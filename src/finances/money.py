from __future__ import annotations

from dataclasses import dataclass

CENTS_PER_DOLLAR = 100

@dataclass(frozen=True)
class Money:
    _cents: int

    @staticmethod
    def of(dollars: int, cents: int) -> Money:
        assert cents >= 0 and cents < CENTS_PER_DOLLAR, (
            f"cents must be between 0 and {CENTS_PER_DOLLAR}"
        )

        if dollars < 0:
            # E.g. -4, 53 becomes -453
            return Money(dollars * CENTS_PER_DOLLAR - cents)
        else:
            return Money(dollars * CENTS_PER_DOLLAR + cents)

    def truncated_dollars(self) -> int:
        return int(self._cents / CENTS_PER_DOLLAR)

    def extra_cents(self) -> int:
        return (
            self._cents % CENTS_PER_DOLLAR + CENTS_PER_DOLLAR
        ) % CENTS_PER_DOLLAR

    def all_cents(self) -> int:
        return self._cents

    def __str__(self) -> str:
        return f"${self.truncated_dollars()}.{self.extra_cents():02}"

    def __add__(self, other: Money) -> Money:
        return Money(self._cents + other._cents)

    def __sub__(self, other: Money) -> Money:
        return Money(self._cents - other._cents)

    def __mul__(self, other: int) -> Money:
        return Money(self._cents * other)

    def grow_and_round(self, ratio: float) -> Money:
        return Money(round(self._cents * ratio))

ZERO = Money.of(0, 0)
