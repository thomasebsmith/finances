"""Types and functions for dealing with numeric distributions."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Protocol, TypeVar

from finances import AddableComparable, Range


_RangeT = TypeVar("_RangeT", bound=AddableComparable)
_ValueT = TypeVar("_ValueT", bound=AddableComparable)


class Distribution(Protocol, Generic[_RangeT, _ValueT]):
    """
    A type that stores numeric distributions.

    Types that fulfill this protocol must expose frozen/constant semantics.
    """

    def value(self, at_point: _RangeT) -> _ValueT:
        """Returns the value at the given point."""

    def average(self, in_range: Range[_RangeT]) -> _ValueT:
        """Returns the average value in the given range."""

    def __add__(
        self, other: Distribution[_RangeT, _ValueT]
    ) -> Distribution[_RangeT, _ValueT]:
        """Returns the sum of this distribution and other."""
        return _SumDistribution(self, other)


@dataclass(eq=False, frozen=True)
class _SumDistribution(Distribution, Generic[_RangeT, _ValueT]):
    """A sum of two Distributions."""

    _dist_1: Distribution[_RangeT, _ValueT]
    _dist_2: Distribution[_RangeT, _ValueT]

    def value(self, at_point: _RangeT) -> _ValueT:
        return self._dist_1.value(at_point) + self._dist_2.value(at_point)

    def average(self, in_range: Range[_RangeT]) -> _ValueT:
        return self._dist_1.average(in_range) + self._dist_2.average(in_range)


@dataclass(eq=False, frozen=True)
class _ProductDistribution(Distribution, Generic[_RangeT, _ValueT]):
    """A product of a distribution and an integer."""

    _dist: Distribution[_RangeT, _ValueT]
    _multiplier: int

    def value(self, at_point: _RangeT) -> _ValueT:
        return self._dist.value(at_point) * self._multiplier

    def average(self, in_range: Range[_RangeT]) -> _ValueT:
        return self._dist.average(in_range) * self._multiplier
