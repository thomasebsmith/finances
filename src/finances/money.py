"""Classes for representing money in U.S. dollars."""

from __future__ import annotations

from dataclasses import dataclass
from typing import cast, ClassVar, Optional

CENTS_PER_DOLLAR = 100


_DIGITS = frozenset(map(str, range(0, 10)))


class _NegativeZeroMarker:
    pass


NEGATIVE_ZERO = _NegativeZeroMarker()


def _parse_nonnegative_int(
    int_string: str, expected_length: Optional[int] = None
) -> int:
    if expected_length is not None and len(int_string) is not expected_length:
        raise ValueError(
            f"Expected {expected_length} characters, but got {len(int_string)}"
        )

    for char in int_string:
        if char not in _DIGITS:
            raise ValueError(f"Unexpected character {char}")

    return int(int_string)


@dataclass(frozen=True, order=True)
class Money:
    """Represents an amount of U.S. dollars, positive, negative, or zero."""

    _cents: int

    ZERO: ClassVar[Money]

    @staticmethod
    def of(dollars: int | _NegativeZeroMarker, cents: int = 0) -> Money:
        """
        Creates Money with the given number of dollars and cents.

        To create negative Money, use negative dollars and non-negative cents.

        Arguments:
            dollars: How many dollars the Money should contain.
            cents: How many cents the Money should contain. Defaults to 0. Must
                   be from 0-99 inclusive.
        Return value: The specified Money.
        """
        if not 0 <= cents < CENTS_PER_DOLLAR:
            raise ValueError(f"cents must be between 0 and {CENTS_PER_DOLLAR}")

        is_negative_zero = isinstance(dollars, _NegativeZeroMarker)
        num_dollars = 0 if is_negative_zero else cast(int, dollars)

        if is_negative_zero or num_dollars < 0:
            # E.g. -4, 53 becomes -453
            return Money(num_dollars * CENTS_PER_DOLLAR - cents)
        else:
            return Money(num_dollars * CENTS_PER_DOLLAR + cents)

    @staticmethod
    def parse(money_string: str) -> Money:
        """
        Parses a string in the form $X.XX to create a Money object.

        Arguments:
            money_string - The string to parse.
        Return value: A Money object representing the parsed value.
        """
        # Remove whitespace
        money_string = money_string.strip()

        # Remove - if it exists
        negate = money_string.startswith("-")
        if negate:
            money_string = money_string[1:]

        # Remove $
        if not money_string.startswith("$"):
            raise ValueError("Money must start with $")
        money_string = money_string[1:]

        # Separate by .
        components = money_string.split(".")

        if len(components) == 1:
            dollars = _parse_nonnegative_int(components[0])
            cents = 0
        elif len(components) == 2:
            dollars = _parse_nonnegative_int(components[0])
            cents = _parse_nonnegative_int(components[1], 2)
        else:
            raise ValueError("Too many dots in money")

        if negate:
            dollars = -dollars

        return Money.of(dollars, cents)

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
        remainder = self._cents % CENTS_PER_DOLLAR

        if self._cents >= 0:
            return remainder
        elif remainder == 0:
            return 0
        else:
            return abs(remainder - CENTS_PER_DOLLAR)

    def all_cents(self) -> int:
        """Returns the total number of cents this Money has."""
        return self._cents

    def __str__(self) -> str:
        """Creates a string representation of this Money using $XX.XX syntax."""
        if self._cents >= 0:
            return f"${self.truncated_dollars()}.{self.extra_cents():02}"
        else:
            return f"-${-self.truncated_dollars()}.{self.extra_cents():02}"

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


Money.ZERO = Money.of(0)
