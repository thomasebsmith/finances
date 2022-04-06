from __future__ import annotations

from dataclasses import dataclass

from .money import Money

@dataclass(frozen=True, order=True)
class Value:
    _year_2000_usd_cents: int

    @staticmethod
    def of_inflated_money(money: Money, inflation: float) -> Value:
        return Value(round(money.all_cents() / (1.0 + inflation)))

    def inflate(self, inflation: float) -> Money:
        return Money(round(self._year_2000_usd_cents * (1.0 + inflation)))

    def __str__(self) -> str:
        return f"{Money(self._year_2000_usd_cents)} @ 2000-01-01"

    def __add__(self, other: Value) -> Value:
        return Value(self._year_2000_usd_cents + other._year_2000_usd_cents)

    def __sub__(self, other: Value) -> Value:
        return Value(self._year_2000_usd_cents - other._year_2000_usd_cents)

    def __mul__(self, other: int) -> Value:
        return Value(self._year_2000_usd_cents * other)

ZERO = Value(0)
