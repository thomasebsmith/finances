"""Contains a class that represents a probability."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import ClassVar

from .errors import SimulationInternalError


@dataclass(frozen=True, order=True)
class Probability:
    """Represents the probability of an event, where 0 is 0% and 1 is 100%."""

    _value: Fraction

    ZERO: ClassVar[Probability]
    ONE: ClassVar[Probability]

    def __post_init__(self) -> None:
        """Checks that self._value is between 0 and 1."""
        if self._value < 0 or self._value > 1:
            raise SimulationInternalError(f"Invalid probability {self._value}")

    def value(self) -> Fraction:
        """Returns this probability's value (in the range 0-1)."""
        return self._value

    def __add__(self, other: Probability) -> Probability:
        """Determines the probability of either of two disjoint events."""
        # __post_init__ will check that this is valid
        return Probability(self._value + other._value)

    def __mul__(self, other: Probability) -> Probability:
        """Determines the probability of both of two independent events."""
        return Probability(self._value * other._value)


Probability.ZERO = Probability(Fraction(0))
Probability.ONE = Probability(Fraction(1))
