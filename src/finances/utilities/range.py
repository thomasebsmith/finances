"""Classes and functions related to contiguous ranges."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import ClassVar, Generic, TypeVar, Union

from .protocols import Comparable


_RangeT = TypeVar("_RangeT", bound=Comparable)


class _NegInfT(Enum):
    VALUE = 0


class _PosInfT(Enum):
    VALUE = 0


_NEGATIVE_INFINITY = _NegInfT.VALUE
_POSITIVE_INFINITY = _PosInfT.VALUE


@dataclass(frozen=True)
class Range(Generic[_RangeT]):
    """
    Represents a range between two values.

    Start is inclusive, and end is exclusive.

    If start or end is None, that bound does not apply.
    """

    NEGATIVE_INFINITY: ClassVar[_NegInfT] = _NEGATIVE_INFINITY
    POSITIVE_INFINITY: ClassVar[_PosInfT] = _POSITIVE_INFINITY

    start: Union[_RangeT, _NegInfT]
    end: Union[_RangeT, _PosInfT]

    def __post_init__(self) -> None:
        """Checks that self.end >= self.start."""
        if (
            self.start is Range.NEGATIVE_INFINITY
            or self.end is Range.POSITIVE_INFINITY
        ):
            return
        if self.start > self.end:
            raise ValueError(f"Start {self.start} is after end {self.end}")

    def contains(self, point: _RangeT) -> bool:
        """Returns whether this range contains the given point."""
        return Range._less_than_or_equal(self.start, point) and Range._less(
            point, self.end
        )

    def surrounds(self, other: Range[_RangeT]) -> bool:
        """Returns whether this range contains the entirety of other."""
        return Range._less_than_or_equal(
            self.start, other.start
        ) and Range._less_than_or_equal(other.end, self.end)

    def near(self, other: Range[_RangeT]) -> bool:
        """Returns whether this range is adjacent to or overlaps with other."""
        return Range._less_than_or_equal(
            self.start, other.end
        ) and Range._less_than_or_equal(other.start, self.end)

    def union(self, other: Range[_RangeT]) -> Range[_RangeT]:
        """Returns the union of this range and other."""
        start: Union[_RangeT, _NegInfT]
        if (
            self.start is Range.NEGATIVE_INFINITY
            or other.start is Range.NEGATIVE_INFINITY
        ):
            start = Range.NEGATIVE_INFINITY
        else:
            start = min(self.start, other.start)

        end: Union[_RangeT, _PosInfT]
        if (
            self.end is Range.POSITIVE_INFINITY
            or other.end is Range.POSITIVE_INFINITY
        ):
            end = Range.POSITIVE_INFINITY
        else:
            end = max(self.end, other.end)

        return Range[_RangeT](start, end)

    def intersection(self, other: Range[_RangeT]) -> Range[_RangeT]:
        """Returns the intersection of this range and other."""
        if self.start is Range.NEGATIVE_INFINITY:
            start = other.start
        elif other.start is Range.NEGATIVE_INFINITY:
            start = self.start
        else:
            start = max(self.start, other.start)

        if self.end is Range.POSITIVE_INFINITY:
            end = other.end
        elif other.end is Range.POSITIVE_INFINITY:
            end = self.end
        else:
            end = min(self.end, other.end)

        if (
            start is not Range.NEGATIVE_INFINITY
            and end is not Range.POSITIVE_INFINITY
            and start > end
        ):
            end = start

        return Range[_RangeT](start, end)

    @staticmethod
    def _less(
        val1: Union[_RangeT, _NegInfT, _PosInfT],
        val2: Union[_RangeT, _NegInfT, _PosInfT],
    ) -> bool:
        if val1 is Range.POSITIVE_INFINITY:
            return False
        if val2 is Range.NEGATIVE_INFINITY:
            return False
        if val1 is Range.NEGATIVE_INFINITY:
            return True
        if val2 is Range.POSITIVE_INFINITY:
            return True
        return val1 < val2

    @staticmethod
    def _less_than_or_equal(
        val1: Union[_RangeT, _NegInfT, _PosInfT],
        val2: Union[_RangeT, _NegInfT, _PosInfT],
    ) -> bool:
        return not Range._less(val1=val2, val2=val1)
