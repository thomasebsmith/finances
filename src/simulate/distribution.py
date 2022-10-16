"""Types and functions for dealing with numeric distributions."""
from dataclasses import dataclass
from typing import Generic, Protocol, TypeVar

from finances import AddableComparable, Range


_RangeT_contra = TypeVar(
    "_RangeT_contra", bound=AddableComparable, contravariant=True
)
_ValueT_co = TypeVar("_ValueT_co", bound=AddableComparable, covariant=True)


class Distribution(Protocol, Generic[_RangeT_contra, _ValueT_co]):
    """
    A type that stores numeric distributions.

    Types that fulfill this protocol must expose frozen/constant semantics.
    """

    def value(self, at_point: _RangeT_contra) -> _ValueT_co:
        """Returns the value at the given point."""

    def average(self, in_range: Range[_RangeT_contra]) -> _ValueT_co:
        """Returns the average value in the given range."""


@dataclass(eq=False, frozen=True)
class _SumDistribution(Distribution, Generic[_RangeT_contra, _ValueT_co]):
    """A sum of two Distributions."""

    _dist_1: Distribution[_RangeT_contra, _ValueT_co]
    _dist_2: Distribution[_RangeT_contra, _ValueT_co]

    def value(self, at_point: _RangeT_contra) -> _ValueT_co:
        return self._dist_1.value(at_point) + self._dist_2.value(at_point)

    def average(self, in_range: Range[_RangeT_contra]) -> _ValueT_co:
        return self._dist_1.average(in_range) + self._dist_2.average(in_range)
