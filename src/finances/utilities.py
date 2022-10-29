"""Utility classes and functions that are not directly related to finances."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Optional, Protocol, TypeVar


# TODO(Python3.11): use Self instead of this
AddableT = TypeVar("AddableT", bound="Addable")


class Addable(Protocol):
    """
    A type that can be added to itself.

    It must have immutable semantics.
    """

    def __add__(self: AddableT, other: AddableT) -> AddableT:
        """Adds two of this type."""

    def __sub__(self: AddableT, other: AddableT) -> AddableT:
        """Subtracts one of this type from this instance."""

    def __mul__(self: AddableT, other: int) -> AddableT:
        """Multiplies this instance by other."""

    def grow_and_round(self: AddableT, ratio: float) -> AddableT:
        """Multiplies this instance by ratio, rounding."""


ComparableT = TypeVar("ComparableT", bound="Comparable")


class Comparable(Protocol):
    """A type that can be compared with itself."""

    def __eq__(self: ComparableT, other: object) -> bool:
        """Checks whether self is equal to other."""

    def __lt__(self: ComparableT, other: ComparableT) -> bool:
        """Checks whether self is less than other."""

    def __le__(self: ComparableT, other: ComparableT) -> bool:
        """Checks whether self is less than or equal to other."""

    def __gt__(self: ComparableT, other: ComparableT) -> bool:
        """Checks whether self is greater than other."""

    def __ge__(self: ComparableT, other: ComparableT) -> bool:
        """Checks whether self is greater than or equal to other."""


class AddableComparable(Addable, Comparable, Protocol):
    """A type that is both Addable and Comparable."""


_RangeT = TypeVar("_RangeT", bound=AddableComparable)


@dataclass(frozen=True)
class Range(Generic[_RangeT]):
    """
    Represents a range between two values.

    Start is inclusive, and end is exclusive.

    If start or end is None, that bound does not apply.
    """

    start: Optional[_RangeT]
    end: Optional[_RangeT]

    def __post_init__(self) -> None:
        """Checks that self.end >= self.start."""
        if self.start is None or self.end is None:
            return
        if self.start > self.end:
            raise ValueError(f"Start {self.start} is after end {self.end}")

    def contains(self, point: _RangeT) -> bool:
        """Returns whether this range contains the given point."""
        if self.start is not None and point < self.start:
            return False
        if self.end is not None and point >= self.end:
            return False
        return True

    def surrounds(self, other: Range[_RangeT]) -> bool:
        """Returns whether this range contains the entirety of other."""
        if self.start is not None:
            if other.start is None:
                return False
            if other.start < self.start:
                return False
        if self.end is not None:
            if other.end is None:
                return False
            if other.end > self.end:
                return False
        return True

    def union(self, other: Range[_RangeT]) -> Range[_RangeT]:
        """Returns the union of this range and other."""
        if self.start is None or other.start is None:
            start = None
        else:
            start = min(self.start, other.start)

        if self.end is None or other.end is None:
            end = None
        else:
            end = max(self.end, other.end)

        return Range[_RangeT](start, end)

    def intersection(self, other: Range[_RangeT]) -> Range[_RangeT]:
        """Returns the intersection of this range and other."""
        if self.start is None:
            start = other.start
        elif other.start is None:
            start = self.start
        else:
            start = max(self.start, other.start)

        if self.end is None:
            end = other.end
        elif other.end is None:
            end = self.end
        else:
            end = min(self.end, other.end)

        if start is not None and end is not None and start > end:
            end = start

        return Range[_RangeT](start, end)

    @staticmethod
    def _less(val1: Optional[_RangeT], val2: Optional[_RangeT]) -> bool:
        if val2 is None:
            return False
        return val1 is None or val1 < val2
