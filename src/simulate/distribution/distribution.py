"""The Distribution protocol."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Protocol, Union, TypeVar, overload

from finances import AddableComparable, Range

from ..errors import SimulationInternalError


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

    def is_in_range(self, point: _RangeT) -> bool:
        """Returns whether the given point is in range for the distribution."""
        return True

    def __add__(
        self, other: Distribution[_RangeT, _ValueT]
    ) -> Distribution[_RangeT, _ValueT]:
        """Returns the sum of this distribution and other."""
        return _SumDistribution(self, other)

    def __mul__(self, multiplier: int) -> Distribution[_RangeT, _ValueT]:
        """Returns the product of this distribution and multiplier."""
        return _ProductDistribution(self, multiplier)

    @overload
    def __getitem__(self, key: _RangeT) -> _ValueT:
        """Returns the value at the given point."""

    @overload
    def __getitem__(
        self,
        key: Range[_RangeT],
    ) -> Distribution[_RangeT, _ValueT]:
        """Returns a subdistribution over the given range."""

    def __getitem__(
        self,
        key: Union[_RangeT, Range[_RangeT]],
    ) -> Union[_ValueT, Distribution[_RangeT, _ValueT]]:
        if isinstance(key, Range):
            return _SubsetDistribution(self, key)
        else:  # key: _RangeT
            return self.value(at_point=key)


@dataclass(eq=False, frozen=True)
class _SumDistribution(Distribution[_RangeT, _ValueT]):
    """A sum of two Distributions."""

    _dist_1: Distribution[_RangeT, _ValueT]
    _dist_2: Distribution[_RangeT, _ValueT]

    def value(self, at_point: _RangeT) -> _ValueT:
        return self._dist_1.value(at_point) + self._dist_2.value(at_point)

    def average(self, in_range: Range[_RangeT]) -> _ValueT:
        return self._dist_1.average(in_range) + self._dist_2.average(in_range)


@dataclass(eq=False, frozen=True)
class _ProductDistribution(Distribution[_RangeT, _ValueT]):
    """A product of a distribution and an integer."""

    _dist: Distribution[_RangeT, _ValueT]
    _multiplier: int

    def value(self, at_point: _RangeT) -> _ValueT:
        return self._dist.value(at_point) * self._multiplier

    def average(self, in_range: Range[_RangeT]) -> _ValueT:
        return self._dist.average(in_range) * self._multiplier


@dataclass(eq=False, frozen=True)
class _SubsetDistribution(Distribution[_RangeT, _ValueT]):
    """A subset of another distribution."""

    _dist: Distribution[_RangeT, _ValueT]
    _range: Range[_RangeT]

    def value(self, at_point: _RangeT) -> _ValueT:
        if not self._range.contains(at_point):
            raise SimulationInternalError(
                f"{at_point} is out of range for subset distribution with range"
                f" {self._range}"
            )
        return self._dist.value(at_point)

    def average(self, in_range: Range[_RangeT]) -> _ValueT:
        if not self._range.surrounds(in_range):
            raise SimulationInternalError(
                f"{in_range} is out of range for subset distribution with range"
                f" {self._range}"
            )
        return self._dist.average(in_range)

    def is_in_range(self, point: _RangeT) -> bool:
        return self._range.contains(point)
