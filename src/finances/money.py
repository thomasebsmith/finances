"""Classes for representing money in U.S. dollars."""

from __future__ import annotations

from dataclasses import dataclass

CENTS_PER_DOLLAR = 100

@dataclass(frozen=True, order=True)
class Money:
    """Represents an amount of U.S. dollars, positive, negative, or zero."""
    _cents: int

    @staticmethod
    def of(dollars: int, cents: int = 0) -> Money:
        """
        Creates Money with the given number of dollars and cents.

        To create negative Money, use negative dollars and non-negative cents.

        Arguments:
            dollars: How many dollars the Money should contain.
            cents: How many cents the Money should contain. Defaults to 0. Must
                   be from 0-99 inclusive.
        Return value: The specified Money.
        """
        assert 0 <= cents < CENTS_PER_DOLLAR, (
            f"cents must be between 0 and {CENTS_PER_DOLLAR}"
        )

        if dollars < 0:
            # E.g. -4, 53 becomes -453
            return Money(dollars * CENTS_PER_DOLLAR - cents)
        else:
            return Money(dollars * CENTS_PER_DOLLAR + cents)

    def truncated_dollars(self) -> int:
        """
        Returns the number of dollars in this Money, excluding any cents.

        Return value: The number of dollars, positive, negative, or zero.
        """
        return int(self._cents / CENTS_PER_DOLLAR)

    def extra_cents(self) -> int:
        """
        Returns the number of cents this Money has beyond its dollars.

        This will always be positive even if this Money is negative.

        Return value: The number of extra cents, from 0-99 inclusive.
        """
        return abs(self._cents % CENTS_PER_DOLLAR)

    def all_cents(self) -> int:
        """Returns the total number of cents this Money has."""
        return self._cents

    def __str__(self) -> str:
        """Creates a string representation of this Money using $XX.XX syntax."""
        return f"${self.truncated_dollars()}.{self.extra_cents():02}"

    def __add__(self, other: Money) -> Money:
        """Creates a new Money with the sum of this Money and other."""
        return Money(self._cents + other._cents)

    def __sub__(self, other: Money) -> Money:
        """Creates a new Money with the difference of this Money and other."""
        return Money(self._cents - other._cents)

    def __mul__(self, other: int) -> Money:
        """Creates a new Money with this Money's amount multiplied by other."""
        return Money(self._cents * other)

    def grow_and_round(self, ratio: float) -> Money:
        """
        Creates a new Money, multiplying by ratio and rounding.

        Rounding is to the nearest cent.

        Arguments:
            ratio: The number by which to multiply this Money's amount.
        Return value: A new Money representing this Money times ratio.
        """
        return Money(round(self._cents * ratio))

ZERO = Money.of(0, 0)
