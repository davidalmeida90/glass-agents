"""Forward test bookkeeping: the track record's migration and the long-short scoring. Offline, no prices fetched."""

import csv
import sys
from datetime import date, timedelta
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # track.py sits at the repo root

import track  # noqa: E402

OLD_HEADER = ["run", "date", "ticker", "rating", "confidence", "uncertainty", "model", "price", "price_date", "bear",
              "base", "bull", "price_to_fair", "target_weight"]


def _old_file(path: Path) -> None:
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(OLD_HEADER)
        w.writerow(["20261001-053519", "2026-10-01", "MSFT", "Hold", "1.0", "High", "fcff", "512.9", "2026-09-30",
                    "265.04", "507.24", "714.26", "1.0112", "0.0"])
        w.writerow(["20261001-053519", "2026-10-01", "O", "Buy", "1.0", "Low", "ddm", "54.3", "2026-09-30",
                    "55.53", "69.11", "87.18", "0.7857", "0.075"])


def _memo(ticker: str, rating: str, price: float = 100.0, base: float = 100.0) -> dict:
    fv = {"bear": base * 0.6, "base": base, "bull": base * 1.4}
    return {"ticker": ticker, "rating": rating, "confidence": 1.0, "sizing": {"weight": 0.0},
            "valuation": {"model": "fcff", "price": price, "price_date": "2026-10-16", "fair_value": fv},
            "repeats": [{"final": {"rating": rating, "uncertainty": "High"}}]}


def test_old_rows_read_as_full_on_the_legacy_snapshot(tmp_path):
    f = tmp_path / "track.csv"
    _old_file(f)
    rows = track.load(f)
    assert [(r["variant"], r["model_snapshot"]) for r in rows] == [("full", "deepseek-v4.1-flash-0910")] * 2
    assert rows[0]["rating"] == "Hold" and rows[1]["price_to_fair"] == "0.7857"


def test_migration_rewrites_the_header_once_and_keeps_every_value(tmp_path):
    f = tmp_path / "track.csv"
    _old_file(f)
    before = list(csv.DictReader(open(f, encoding="utf-8")))
    assert track.migrate(f) == 2
    assert track.migrate(f) == 0  # already current
    with open(f, encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        assert reader.fieldnames == track.FIELDS
        after = list(reader)
    assert [{k: r[k] for k in OLD_HEADER} for r in after] == before
    assert {(r["variant"], r["model_snapshot"]) for r in after} == {("full", "deepseek-v4.1-flash-0910")}


def test_record_migrates_then_appends_both_variants_aligned(tmp_path):
    f = tmp_path / "track.csv"
    _old_file(f)
    memos = [_memo("MSFT", "Hold"), _memo("AAPL", "Sell", 130, 100)]
    assert track.record("r-code", memos, "code", "ignored for code", path=f) == 2
    cut = dict(_memo("KO", "Buy"), cut_by_budget=True)
    assert track.record("r-full", memos + [cut], "full", "deepseek-v4.1-flash-1017", path=f) == 2
    assert track.record("r-full", memos, "full", "deepseek-v4.1-flash-1017", path=f) == 0  # same run twice
    rows = track.load(f)
    assert len(rows) == 6
    assert [(r["ticker"], r["variant"], r["model_snapshot"]) for r in rows[2:]] == [
        ("MSFT", "code", ""), ("AAPL", "code", ""),
        ("MSFT", "full", "deepseek-v4.1-flash-1017"), ("AAPL", "full", "deepseek-v4.1-flash-1017")]
    assert rows[3]["price_to_fair"] == "1.3"


def test_snapshot_is_declared_when_the_api_names_only_the_alias():
    assert track.snapshot(["deepseek-flash"], "deepseek-flash") == track.SNAPSHOTS["deepseek-flash"]
    assert track.snapshot([], "deepseek-flash") == track.SNAPSHOTS["deepseek-flash"]
    assert track.snapshot(["deepseek-flash", "deepseek-v4.2-flash-1201"], "deepseek-flash") == "deepseek-v4.2-flash-1201"


def test_close_on_takes_the_last_close_on_or_before():
    s = [("2026-01-02", 1.0), ("2026-01-05", 2.0), ("2026-01-06", 3.0)]
    assert track.close_on(s, "2026-01-04") == ("2026-01-02", 1.0)
    assert track.close_on(s, "2026-01-05") == ("2026-01-05", 2.0)
    assert track.close_on(s, "2026-01-01") is None


def _daily(start: str, days: int, total: float) -> list[tuple[str, float]]:
    """Calendar-daily closes growing smoothly to 1 + total at the end."""
    d0 = date.fromisoformat(start)
    return [((d0 + timedelta(days=i)).isoformat(), 100 * (1 + total) ** (i / days)) for i in range(days + 1)]


def test_excess_return_over_a_fixed_horizon_not_to_today():
    prices = {"SPY": _daily("2026-01-01", 400, 0.10), "A": _daily("2026-01-01", 400, 0.30)}
    row = {"ticker": "A", "price_date": "2026-01-01"}
    x90 = track.excess_return(row, 90, prices.__getitem__)
    assert x90 == pytest.approx(1.3 ** (90 / 400) - 1.1 ** (90 / 400))
    assert track.excess_return({"ticker": "A", "price_date": "2027-03-01"}, 90, prices.__getitem__) is None  # no later close


def test_long_short_is_longs_minus_shorts_with_hits():
    s = track.long_short([("Buy", 0.10), ("Overweight", -0.02), ("Hold", 0.50), ("Underweight", -0.04), ("Sell", 0.02)])
    assert s["long"] == pytest.approx(0.04) and s["short"] == pytest.approx(-0.01)
    assert s["long_short"] == pytest.approx(0.05)
    assert (s["long_n"], s["short_n"], s["hold_n"]) == (2, 2, 1)
    assert (s["long_hits"], s["short_hits"], s["hits"]) == (1, 1, 2)
    assert track.long_short([("Buy", 0.1), ("Hold", 0.0)])["long_short"] is None  # no short leg


def _row(ticker, rating, variant, snap="", day="2026-01-01", run="r1"):
    return {"run": run, "date": day, "ticker": ticker, "rating": rating, "price_date": day, "variant": variant,
            "model_snapshot": snap}


def test_score_rows_by_variant_only_when_old_enough_and_paired_with_code():
    prices = {"SPY": _daily("2026-01-01", 400, 0.0), "A": _daily("2026-01-01", 400, 0.20),
              "B": _daily("2026-01-01", 400, -0.20), "C": _daily("2026-01-01", 400, 0.10)}
    snap = "deepseek-v4.1-flash-1017"
    rows = [_row("A", "Buy", "full", snap), _row("B", "Sell", "full", snap), _row("C", "Hold", "full", snap),
            _row("A", "Sell", "code", run="r0"),  # an earlier run the same day: replaced by the day's last
            _row("A", "Hold", "code"), _row("B", "Buy", "code"),
            _row("C", "Buy", "full", "deepseek-v4.1-flash-0910")]
    res = track.score_rows(rows, 90, prices.__getitem__, today=date(2026, 6, 1))
    assert set(res) == {"code", f"full / {snap}", "full / deepseek-v4.1-flash-0910"}
    full = res[f"full / {snap}"]
    a, b = 1.2 ** (90 / 400) - 1, 0.8 ** (90 / 400) - 1
    assert full["all"]["long_short"] == pytest.approx(a - b) and full["all"]["hits"] == 2
    assert full["code_same"]["n"] == 2 and full["code_same"]["long"] == pytest.approx(b)  # code rated B a Buy
    assert full["code_same"]["long_short"] is None  # code has no short on these names
    assert res["code"]["all"]["hold_n"] == 1
    assert res["full / deepseek-v4.1-flash-0910"]["code_same"] is None
    assert track.score_rows(rows, 180, prices.__getitem__, today=date(2026, 6, 1)) == {}  # not old enough
