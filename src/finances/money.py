from __future__ import annotations

from dataclasses import dataclass

CENTS_PER_DOLLAR = 100

@dataclass(frozen=True)
class Money:
    _cents: int

    def floored_dollars(self) -> int:
        return int(self._cents / CENTS_PER_DOLLAR)

    def extra_cents(self) -> int:
        return (
            self._cents % CENTS_PER_DOLLAR + CENTS_PER_DOLLAR
        ) % CENTS_PER_DOLLAR

    def all_cents(self) -> int:
        return self._cents

    def __str__(self) -> str:
        return f"${self.floored_dollars()}.{self.extra_cents()}"

    def __add__(self, other: Money) -> Money:
        return Money(self._cents + other._cents)

    def __sub__(self, other: Money) -> Money:
        return Money(self._cents - other._cents)

    def __mul__(self, other: int) -> Money:
        return Money(self._cents * other)

    def grow_and_round(self, ratio: float) -> Money:
        return Money(round(self._cents * ratio))

ZERO = Money(0)
