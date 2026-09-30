"""Position size in code: the rating sets a base weight, volatility scales it, the noise meter trims it.

Long-only: Buy 5%, Overweight 3%, anything else 0% (Hold keeps what is held, Underweight and Sell mean
avoid or trim). The base weight is scaled by 25% / annual volatility (a stock twice as volatile gets half
the weight, scaling capped at 1.5x), multiplied by the noise meter's agreement, and capped at 8%.
"""

from __future__ import annotations

import math
from datetime import date, timedelta
from typing import Any

BASE_WEIGHT = {"Buy": 0.05, "Overweight": 0.03}
TARGET_VOL, MAX_SCALE, CAP = 0.25, 1.5, 0.08


def annual_volatility(ticker: str, as_of: str | None = None) -> float | None:
    """Annualised volatility of daily log returns over the past year, from Yahoo closes."""
    import yfinance as yf

    end = date.fromisoformat(as_of) if as_of else date.today()
    hist = yf.Ticker(ticker).history(start=(end - timedelta(days=370)).isoformat(),
                                     end=(end + timedelta(days=1)).isoformat(), auto_adjust=True)
    closes = [float(c) for c in hist["Close"] if c and c > 0]
    if len(closes) < 60:
        return None
    rets = [math.log(b / a) for a, b in zip(closes, closes[1:])]
    mean = sum(rets) / len(rets)
    var = sum((r - mean) ** 2 for r in rets) / (len(rets) - 1)
    return math.sqrt(var) * math.sqrt(252)


def size(rating: str, confidence: float, vol: float | None) -> dict[str, Any]:
    base = BASE_WEIGHT.get(rating, 0.0)
    if base == 0.0 or not vol:
        return {"weight": 0.0, "base": base, "vol": vol, "scale": None, "confidence": confidence}
    scale = min(TARGET_VOL / vol, MAX_SCALE)
    return {"weight": round(min(base * scale * confidence, CAP), 4), "base": base, "vol": round(vol, 4),
            "scale": round(scale, 3), "confidence": confidence}
