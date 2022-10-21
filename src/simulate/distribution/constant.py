"""Classes and functions related to constant distributions."""

from dataclasses import dataclass
from typing import TypeVar

from finances import AddableComparable, Range

from .distribution import Distribution


_RangeT = TypeVar("_RangeT", bound=AddableComparable)
_ValueT = TypeVar("_ValueT", bound=AddableComparable)


@dataclass(eq=False, frozen=True)
class ConstantDistribution(Distribution[_RangeT, _ValueT]):
    """A distribution with a constant value at every point."""

    constant_value: _ValueT

    def value(self, at_point: _RangeT) -> _ValueT:
        return self.constant_value

    def average(self, in_range: Range[_RangeT]) -> _ValueT:
        return self.constant_value
