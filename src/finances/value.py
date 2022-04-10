"""Contains classes for representing time-independent financial values."""

from __future__ import annotations

from dataclasses import dataclass

from .money import Money


@dataclass(frozen=True, order=True)
class Value:
    """Represents a financial value, independent of time."""

    _year_2000_usd_cents: int

    @staticmethod
    def of_inflated_money(money: Money, inflation_since_2000: float) -> Value:
        """
        Creates a Value based on some amount of money at a point in time.

        Arguments:
            money - The amount of money.
            inflation_since_2000 - The increase in the cost of goods since
                2000. If costs have decreased, this should be negative.
        Return value: A Value representing this amount of money.
        """
        return Value(round(money.all_cents() / (1.0 + inflation_since_2000)))

    def inflate(self, inflation_since_2000: float) -> Money:
        """
        Returns the amount of Money contained in this Value after inflation.

        Arguments:
            inflation_since_2000: The amount of inflation since the year 2000.
        Return value: How much money this Value will be worth after inflation.
        """
        return Money(
            round(self._year_2000_usd_cents * (1.0 + inflation_since_2000))
        )

    def __str__(self) -> str:
        """Creates a string representation of this Value."""
        return f"{Money(self._year_2000_usd_cents)} @ 2000-01-01"

    def __add__(self, other: Value) -> Value:
        """Creates a new Value with the sum of this Value and other."""
        return Value(self._year_2000_usd_cents + other._year_2000_usd_cents)

    def __sub__(self, other: Value) -> Value:
        """Creates a new Value with the difference of this Value and other."""
        return Value(self._year_2000_usd_cents - other._year_2000_usd_cents)

    def __mul__(self, other: int) -> Value:
        """Creates a new Value with the product of this Value and other."""
        return Value(self._year_2000_usd_cents * other)


ZERO = Value(0)
