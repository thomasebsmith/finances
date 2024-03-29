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

    def range(self) -> Range[_RangeT]:
        """Returns the range of points that are in this distribution."""

    def __add__(
        self, other: Distribution[_RangeT, _ValueT]
    ) -> Distribution[_RangeT, _ValueT]:
        """Returns the sum of this distribution and other."""
        return _SumDistribution(
            self,
            other,
            self.range().intersection(other.range()),
        )

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

    def defaulting_to(
        self, other: Distribution[_RangeT, _ValueT]
    ) -> Distribution[_RangeT, _ValueT]:
        """
        Returns a distribution defaulting to the values in other.

        The values at points outside of this distribution's range default to the
        values at the corresponding points in other.
        """
        return _DefaultingDistribution(
            self,
            other,
            self.range().union(other.range()),
        )


@dataclass(eq=False, frozen=True)
class _SumDistribution(Distribution[_RangeT, _ValueT]):
    """A sum of two Distributions."""

    _dist_1: Distribution[_RangeT, _ValueT]
    _dist_2: Distribution[_RangeT, _ValueT]
    _range: Range[_RangeT]

    def value(self, at_point: _RangeT) -> _ValueT:
        return self._dist_1.value(at_point) + self._dist_2.value(at_point)

    def average(self, in_range: Range[_RangeT]) -> _ValueT:
        return self._dist_1.average(in_range) + self._dist_2.average(in_range)

    def range(self) -> Range[_RangeT]:
        return self._range


@dataclass(eq=False, frozen=True)
class _ProductDistribution(Distribution[_RangeT, _ValueT]):
    """A product of a distribution and an integer."""

    _dist: Distribution[_RangeT, _ValueT]
    _multiplier: int

    def value(self, at_point: _RangeT) -> _ValueT:
        return self._dist.value(at_point) * self._multiplier

    def average(self, in_range: Range[_RangeT]) -> _ValueT:
        return self._dist.average(in_range) * self._multiplier

    def range(self) -> Range[_RangeT]:
        return self._dist.range()


@dataclass(eq=False, frozen=True)
class _SubsetDistribution(Distribution[_RangeT, _ValueT]):
    """A subset of another distribution."""

    _dist: Distribution[_RangeT, _ValueT]
    _range: Range[_RangeT]

    def __post_init__(self) -> None:
        """Checks that _dist contains the entirety of _range."""
        if not self._dist.range().surrounds(self._range):
            raise SimulationInternalError(
                f"Specified range {self._range} is not valid over distribution "
                f"range {self._dist.range()}"
            )

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

    def range(self) -> Range[_RangeT]:
        return self._range


@dataclass(eq=False, frozen=True)
class _DefaultingDistribution(Distribution[_RangeT, _ValueT]):
    """A distribution that defaults to another one as a backup."""

    _primary: Distribution[_RangeT, _ValueT]
    _backup: Distribution[_RangeT, _ValueT]
    _range: Range[_RangeT]

    def __post_init__(self) -> None:
        """Checks that self._primary and self._backup are near each other."""
        if not self._primary.range().near(self._backup.range()):
            raise ValueError(
                f"Primary distribution range {self._primary.range()} is not "
                f"near backup distribution range {self._backup.range()}"
            )

    def value(self, at_point: _RangeT) -> _ValueT:
        if not self._primary.range().contains(at_point):
            return self._backup.value(at_point)
        return self._primary.value(at_point)

    def average(self, in_range: Range[_RangeT]) -> _ValueT:
        if not self._range.surrounds(in_range):
            raise SimulationInternalError(
                f"{in_range} is out of range for defaulting distribution with"
                f" range {self._range}"
            )
        if self._primary.range().surrounds(in_range):
            return self._primary.average(in_range)
        elif not self._primary.range().near(in_range):
            return self._backup.average(in_range)
        raise NotImplementedError()

    def range(self) -> Range[_RangeT]:
        return self._range
