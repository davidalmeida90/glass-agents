"""FCFF discounted cash flow with reinvestment tied to growth (Damodaran's Ginzu structure), in pure functions.

Revenue grows at the starting rate for the high-growth years, then fades linearly to the terminal rate.
Operating margin holds at today's level, or moves linearly to a target margin by a set year (forward
drivers). Tax moves from the effective to the marginal rate. Growth has to be
paid for: reinvestment = change in revenue / sales-to-capital, so a capex-heavy business needs more cash to
grow. FCFF = NOPAT - reinvestment, discounted at WACC (mid-year convention optional). The terminal value
keeps a chosen share of today's excess return: ROIC_T = WACC + share x (ROIC - WACC), and terminal
reinvestment = g / ROIC_T, so growth only adds value when returns exceed the cost of capital.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Any


@dataclass(frozen=True)
class Inputs:
    revenue: float            # trailing twelve months
    ebit: float               # operating income, stock-based compensation already expensed
    effective_tax: float
    marginal_tax: float
    invested_capital: float   # equity + debt + leases - cash and securities
    operating_capital: float  # invested capital without goodwill and acquired intangibles
    growth: float             # starting revenue growth
    terminal_growth: float
    wacc: float
    terminal_excess_return: float
    mature_wacc: float | None  # cost of capital reached by the last fade year; None keeps WACC constant
    high_growth_years: int
    fade_years: int
    mid_year: bool
    debt: float               # including lease liabilities
    cash: float               # cash and marketable securities
    minority: float
    shares: float
    year5_growth_cap: float = 1.0  # growth above this decays to it by year 5 instead of holding (base rates)
    target_margin: float | None = None  # margin reached by margin_years, then held; None holds today's margin
    margin_years: int = 5

    def margin_at(self, t: int) -> float:
        if self.target_margin is None:
            return self.margin
        return self.margin + (self.target_margin - self.margin) * min(t, self.margin_years) / self.margin_years

    @property
    def margin(self) -> float:
        return self.ebit / self.revenue

    @property
    def sales_to_capital(self) -> float:
        return self.revenue / self.operating_capital

    @property
    def roic(self) -> float:
        return self.ebit * (1 - self.effective_tax) / self.invested_capital


def value_per_share(x: Inputs) -> dict[str, Any]:
    """Equity value per share and the pieces behind it."""
    years = x.high_growth_years + x.fade_years
    rev, ev, rows, discount = x.revenue, 0.0, [], 1.0
    end_wacc = x.mature_wacc if x.mature_wacc is not None else x.wacc
    for t in range(1, years + 1):
        if t <= x.high_growth_years:
            rate = x.wacc
        else:
            rate = x.wacc + (end_wacc - x.wacc) * (t - x.high_growth_years) / x.fade_years
        discount /= 1 + rate
        mid = min(x.growth, x.year5_growth_cap)  # the rate reached at the end of the high-growth years
        if t <= x.high_growth_years:
            g = x.growth + (mid - x.growth) * (t - 1) / max(x.high_growth_years - 1, 1)
        else:
            k = t - x.high_growth_years
            g = mid + (x.terminal_growth - mid) * k / x.fade_years
        tax = x.effective_tax + (x.marginal_tax - x.effective_tax) * t / years
        new_rev = rev * (1 + g)
        nopat = new_rev * x.margin_at(t) * (1 - tax)
        reinvestment = (new_rev - rev) / x.sales_to_capital
        fcff = nopat - reinvestment
        ev += fcff * discount
        rows.append({"year": t, "growth": g, "revenue": new_rev, "nopat": nopat, "reinvestment": reinvestment,
                     "fcff": fcff})
        rev = new_rev
    roic_t = end_wacc + x.terminal_excess_return * max(x.roic - end_wacc, 0.0)
    nopat_t = rev * (1 + x.terminal_growth) * x.margin_at(years) * (1 - x.marginal_tax)
    fcff_t = nopat_t * (1 - x.terminal_growth / roic_t)
    terminal = fcff_t / (end_wacc - x.terminal_growth) * discount
    ev += terminal
    if x.mid_year:
        ev *= (1 + x.wacc) ** 0.5
        terminal *= (1 + x.wacc) ** 0.5
    equity = ev - x.debt - x.minority + x.cash
    return {"per_share": equity / x.shares, "enterprise_value": ev, "equity_value": equity,
            "terminal_share": terminal / ev if ev > 0 else None, "terminal_roic": roic_t,
            "ev_to_ebit": ev / x.ebit if x.ebit > 0 else None, "forecast": rows}


def implied_growth(x: Inputs, price: float) -> float | None:
    """Starting revenue growth at which the value per share equals the price (bisection), or None."""
    lo, hi = -0.20, 0.80

    def f(g: float) -> float:
        return value_per_share(replace(x, growth=g))["per_share"] - price

    if f(lo) > 0 or f(hi) < 0:
        return None
    for _ in range(80):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if f(mid) < 0 else (lo, mid)
    return (lo + hi) / 2


def implied_margin(x: Inputs, price: float) -> float | None:
    """Constant operating margin at which the value per share equals the price (bisection), or None."""
    lo, hi = 0.001, 0.9

    def f(m: float) -> float:
        return value_per_share(replace(x, ebit=m * x.revenue, target_margin=None))["per_share"] - price

    if f(lo) > 0 or f(hi) < 0:
        return None
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if f(mid) < 0 else (lo, mid)
    return (lo + hi) / 2


SCENARIO_SHIFTS = {  # growth points, margin (relative), WACC points, terminal excess return share
    "bear": {"growth": -0.04, "margin": -0.10, "wacc": 0.005, "terminal_excess_return": 0.0},
    "base": {"growth": 0.0, "margin": 0.0, "wacc": 0.0, "terminal_excess_return": None},
    "bull": {"growth": 0.04, "margin": 0.10, "wacc": -0.005, "terminal_excess_return": 1.0},
}


def scenario(x: Inputs, name: str) -> Inputs:
    s = SCENARIO_SHIFTS[name]
    ebit = x.ebit * (1 + s["margin"])  # relative: 10% of a 4% margin is 0.4 points, of a 45% margin 4.5
    target = None if x.target_margin is None else x.target_margin * (1 + s["margin"])
    return replace(x, growth=x.growth + s["growth"], ebit=max(ebit, 0.01 * x.revenue), wacc=x.wacc + s["wacc"],
                   target_margin=target,
                   mature_wacc=None if x.mature_wacc is None else x.mature_wacc + s["wacc"],
                   terminal_excess_return=x.terminal_excess_return if s["terminal_excess_return"] is None
                   else s["terminal_excess_return"])


def sensitivity(x: Inputs) -> dict[str, Any]:
    """Base value per share on a WACC x terminal growth grid, and each lever's swing on its own."""
    grid = {f"wacc {dw:+.1%}": {f"g {dg:+.1%}": round(value_per_share(replace(
        x, wacc=x.wacc + dw, terminal_growth=x.terminal_growth + dg))["per_share"], 2)
        for dg in (-0.005, 0.0, 0.005)} for dw in (-0.01, 0.0, 0.01)}
    base = value_per_share(x)["per_share"]
    swings = {}
    for lever in ("growth", "margin", "wacc", "terminal_excess_return"):
        vals = []
        for side in ("bear", "bull"):
            s = dict.fromkeys(("growth", "margin", "wacc"), 0.0) | {"terminal_excess_return": None}
            s[lever] = SCENARIO_SHIFTS[side][lever]
            y = replace(x, growth=x.growth + s["growth"], ebit=max(x.ebit * (1 + s["margin"]), 0.01 * x.revenue),
                        target_margin=None if x.target_margin is None else x.target_margin * (1 + s["margin"]),
                        wacc=x.wacc + s["wacc"], terminal_excess_return=x.terminal_excess_return
                        if s["terminal_excess_return"] is None else s["terminal_excess_return"])
            vals.append(value_per_share(y)["per_share"] - base)
        swings[lever] = [round(v, 2) for v in vals]
    return {"grid": grid, "swings": swings}
