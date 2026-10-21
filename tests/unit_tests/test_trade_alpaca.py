"""trade_alpaca.plan: from ratings and target weights to orders, with no network."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from trade_alpaca import MAX_ORDER, plan  # noqa: E402

EQUITY = 100_000.0


def memo(ticker, rating, weight=0.0):
    return {"ticker": ticker, "rating": rating, "sizing": {"weight": weight}}


def pos(value, qty=10.0, price=None):
    return {"market_value": str(value), "qty": str(qty), "current_price": str(price or value / qty)}


def test_buy_with_nothing_held_buys_the_target_in_dollars():
    (row,) = plan([memo("MSFT", "Buy", 0.05)], EQUITY, {}, set())
    assert row["action"] == "buy" and row["notional"] == 5_000.0


def test_overweight_tops_up_only_the_shortfall():
    (row,) = plan([memo("V", "Overweight", 0.03)], EQUITY, {"V": pos(1_000.0)}, set())
    assert row["action"] == "buy" and row["notional"] == 2_000.0


def test_position_above_target_sells_the_excess():
    (row,) = plan([memo("V", "Overweight", 0.03)], EQUITY, {"V": pos(5_000.0, qty=10, price=500)}, set())
    assert row["action"] == "sell" and row["qty"] == 4.0


def test_hold_keeps_what_is_held():
    (row,) = plan([memo("MSFT", "Hold")], EQUITY, {"MSFT": pos(3_000.0)}, set())
    assert row["action"] == "none"


def test_underweight_sells_everything_held_and_nothing_when_flat():
    held, flat = plan([memo("KO", "Underweight"), memo("AMZN", "Sell")], EQUITY, {"KO": pos(2_000.0, qty=30)}, set())
    assert held["action"] == "sell" and held["qty"] == 30.0
    assert flat["action"] == "none"


def test_small_differences_and_working_orders_are_skipped():
    tiny, busy = plan([memo("META", "Buy", 0.05), memo("NVDA", "Buy", 0.05)], EQUITY,
                      {"META": pos(4_950.0)}, {"NVDA"})
    assert tiny["action"] == "none" and busy["action"] == "none"


def test_no_order_above_the_cap():
    (row,) = plan([memo("X", "Buy", 0.5)], EQUITY, {}, set())
    assert row["notional"] == MAX_ORDER * EQUITY
