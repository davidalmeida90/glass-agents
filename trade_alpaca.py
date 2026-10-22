"""Send a desk batch's decisions to an Alpaca PAPER account.

  python trade_alpaca.py                     plan only: the orders the latest full batch implies, nothing sent
  python trade_alpaca.py --send              send them (asks y/N; --yes skips the question)
  python trade_alpaca.py --memo runs/memo-....json --send --yes
  python trade_alpaca.py --memo "../trading_agents/desk/data/runs/20261022-*/memo.json"   Glassbench run memos
  python trade_alpaca.py --status            account, positions and open orders

What becomes an order (long only, sized by the desk's own rule in sizing.py):
  Buy, Overweight     rebalance to the memo's target weight x account equity; buy the shortfall in dollars
                      (fractional), sell the excess when the position is already above target
  Hold                nothing: keep what is held
  Underweight, Sell   sell the whole position; nothing when nothing is held
Differences under MIN_TRADE dollars are skipped. Orders are market, day; outside market hours Alpaca queues
them for the next open.

Safety: paper keys only (they start with PK) on the paper endpoint, one order per stock per batch (the client
order ID carries the batch stamp, so a second --send of the same batch is refused by Alpaca), a symbol with a
working order is skipped, no order above MAX_ORDER of equity. Keys come from .env (see .env.example) and are never
printed. Every order sent is appended to runs/orders.jsonl.
"""

from __future__ import annotations

import argparse
import glob
import json
import math
import sys
import time
from pathlib import Path

import httpx

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "FIDCS" / "backend"))

PAPER = "https://paper-api.alpaca.markets/v2"
MIN_TRADE = 100.0          # dollars: smaller rebalances are skipped
MAX_ORDER = 0.10           # of equity: no single order above this (the desk caps a position at 8%)
EXIT = {"Underweight", "Sell"}
ADD = {"Buy", "Overweight"}
ORDERS_LOG = HERE / "runs" / "orders.jsonl"


def client() -> httpx.Client:
    from run import key_reader  # chaves on David's machine, else .env in this folder, else the environment

    get, _ = key_reader()
    key, secret = get("ALPACA_API_KEY") or "", get("ALPACA_SECRET_KEY") or ""
    if not key or not secret:
        sys.exit("ALPACA_API_KEY / ALPACA_SECRET_KEY missing: add your paper keys to .env (see .env.example)")
    if not key.startswith("PK"):
        sys.exit("These look like live keys (paper keys start with PK). This script only trades paper accounts.")
    return httpx.Client(base_url=PAPER, timeout=15,
                        headers={"APCA-API-KEY-ID": key, "APCA-API-SECRET-KEY": secret})


def latest_full_batch() -> Path:
    for path in sorted((HERE / "runs").glob("memo-*.json"), reverse=True):
        if json.loads(path.read_text(encoding="utf-8")).get("variant") == "full":
            return path
    sys.exit("no full-variant batch in runs/ (run desk.py first)")


def plan(memos: list[dict], equity: float, positions: dict[str, dict], working: set[str]) -> list[dict]:
    orders = []
    for m in memos:
        t, rating = m["ticker"], m.get("rating") or "no rating"
        pos = positions.get(t)
        held = float(pos["market_value"]) if pos else 0.0
        row = {"ticker": t, "rating": rating, "target_weight": 0.0, "held": round(held, 2), "action": "none"}
        if t in working:
            row["why"] = "a working order already exists"
        elif rating in ADD:
            w = float((m.get("sizing") or {}).get("weight") or 0.0)
            target = w * equity
            row["target_weight"] = w
            delta = target - held
            if delta >= MIN_TRADE:
                row.update(action="buy", notional=round(min(delta, MAX_ORDER * equity), 2))
            elif delta <= -MIN_TRADE and pos:
                price = float(pos["current_price"])
                qty = math.floor(-delta / price * 1e6) / 1e6
                row.update(action="sell", qty=qty, why="above target")
            else:
                row["why"] = "already at target"
        elif rating in EXIT:
            if pos:
                row.update(action="sell", qty=float(pos["qty"]), why="exit")
            else:
                row["why"] = "nothing held"
        else:
            row["why"] = "Hold keeps what is held" if rating == "Hold" else "no rating, no trade"
        orders.append(row)
    return orders


def send(api: httpx.Client, row: dict, stamp: str) -> dict:
    body = {"symbol": row["ticker"], "side": row["action"], "type": "market", "time_in_force": "day",
            "client_order_id": f"fa-{stamp}-{row['ticker']}-{row['action']}"}
    if row["action"] == "buy":
        body["notional"] = f"{row['notional']:.2f}"
    else:
        body["qty"] = f"{row['qty']}"
    res = api.post("/orders", json=body)
    if res.status_code >= 400 and row["action"] == "buy" and "fractional" in res.text.lower():
        # fractional orders refused (asset or session): fall back to whole shares at the last trade price
        last = api.get(f"https://data.alpaca.markets/v2/stocks/{row['ticker']}/trades/latest").json()["trade"]["p"]
        body.pop("notional")
        body["qty"] = str(int(row["notional"] // float(last)))
        res = api.post("/orders", json=body)
    out = {"ticker": row["ticker"], "status_code": res.status_code, "request": body}
    out["response"] = res.json() if res.headers.get("content-type", "").startswith("application/json") else res.text[:300]
    return out


def status(api: httpx.Client) -> None:
    acct = api.get("/account").json()
    print(f"paper account ...{str(acct['account_number'])[-4:]}  {acct['status']}  equity {float(acct['equity']):,.2f}"
          f"  cash {float(acct['cash']):,.2f}  buying power {float(acct['buying_power']):,.2f}")
    for p in api.get("/positions").json():
        print(f"  position {p['symbol']:<6} qty {float(p['qty']):>10.4f}  value {float(p['market_value']):>11,.2f}"
              f"  P&L {float(p['unrealized_pl']):>+9,.2f}")
    for o in api.get("/orders", params={"status": "open"}).json():
        what = o.get("notional") and f"${float(o['notional']):,.2f}" or f"{o['qty']} sh"
        print(f"  open order {o['symbol']:<6} {o['side']:<4} {what:>12}  {o['status']}  {o['client_order_id']}")


def main() -> int:
    ap = argparse.ArgumentParser(description=(__doc__ or "").splitlines()[0])
    ap.add_argument("--memo", nargs="+", help="a desk batch file (runs/memo-*.json) or Glassbench run memos (memo.json), wildcards allowed (default: the latest full batch)")
    ap.add_argument("--send", action="store_true", help="send the orders (default: plan only)")
    ap.add_argument("--yes", action="store_true", help="do not ask before sending")
    ap.add_argument("--status", action="store_true", help="account, positions and open orders, then exit")
    args = ap.parse_args()

    api = client()
    if args.status:
        status(api)
        return 0
    paths = [Path(f) for pat in (args.memo or []) for f in sorted(glob.glob(pat))] or [latest_full_batch()]
    loaded = [json.loads(p.read_text(encoding="utf-8")) for p in paths]
    if len(loaded) == 1 and "memos" in loaded[0]:               # one desk batch
        batch, path = loaded[0], paths[0]
        stamp = path.stem.replace("memo-", "")
    else:                                                       # Glassbench run memos, one company each
        batch = {"variant": "glassbench runs", "model_snapshot": "deepseek-flash",
                 "memos": [m for d in loaded for m in (d["memos"] if "memos" in d else [d])]}
        stamp = "gb-" + time.strftime("%Y%m%d-%H%M%S")
        path = Path(f"{len(paths)} Glassbench runs")
    acct = api.get("/account").json()
    equity = float(acct["equity"])
    positions = {p["symbol"]: p for p in api.get("/positions").json()}
    working = {o["symbol"] for o in api.get("/orders", params={"status": "open"}).json()}
    clock = api.get("/clock").json()
    rows = plan(batch["memos"], equity, positions, working)

    print(f"batch {path.name}  ({batch.get('variant')}, {batch.get('model_snapshot')})  "
          f"paper equity {equity:,.2f}  market {'open' if clock['is_open'] else 'closed, orders queue for ' + clock['next_open'][:16]}")
    for r in rows:
        what = (f"BUY  ${r['notional']:>10,.2f}" if r["action"] == "buy" else
                f"SELL {r['qty']:>10} sh" if r["action"] == "sell" else "     nothing      ")
        print(f"  {r['ticker']:<6} {r['rating']:<12} target {r['target_weight']:>5.1%}  held ${r['held']:>10,.2f}  "
              f"{what}  {r.get('why', '')}")
    todo = [r for r in rows if r["action"] in ("buy", "sell")]
    if not todo:
        print("no orders to send")
        return 0
    if not args.send:
        print(f"plan only: {len(todo)} orders. Add --send to place them on the paper account.")
        return 0
    if not args.yes and input(f"send {len(todo)} orders to the paper account? [y/N] ").strip().lower() != "y":
        print("nothing sent")
        return 0
    ORDERS_LOG.parent.mkdir(exist_ok=True)
    with ORDERS_LOG.open("a", encoding="utf-8") as log:
        for r in todo:
            out = send(api, r, stamp)
            out["batch"], out["at"] = path.name, time.strftime("%Y-%m-%dT%H:%M:%S")
            log.write(json.dumps(out) + "\n")
            resp = out["response"] if isinstance(out["response"], dict) else {}
            print(f"  {r['ticker']:<6} {r['action']:<4} -> HTTP {out['status_code']}  {resp.get('status', '')}"
                  f"  {resp.get('id', '')[:8]}  {'' if out['status_code'] < 400 else str(out['response'])[:160]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
