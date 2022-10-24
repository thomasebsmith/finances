"""Utility classes and functions that are not directly related to finances."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Protocol, TypeVar


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

    Starts is inclusive, and end is exclusive.
    """

    start: _RangeT
    end: _RangeT

    def __post_init__(self) -> None:
        """Checks that self.end >= self.start."""
        if self.start > self.end:
            raise ValueError(f"Start {self.start} is after end {self.end}")

    def contains(self, point: _RangeT) -> bool:
        """Returns whether this range contains the given point."""
        return self.start <= point < self.end

    def surrounds(self, other: Range[_RangeT]) -> bool:
        """Returns whether this range contains the entirety of other."""
        return self.start <= other.start and self.end >= other.end
