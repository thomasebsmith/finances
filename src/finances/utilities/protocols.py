"""General-purpose protocols."""

from __future__ import annotations

from typing import Protocol, TypeVar


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


GrowableT = TypeVar("GrowableT", bound="Growable")


class Growable(AddableComparable, Protocol):
    """A custom type that can be multiplied by a ratio."""

    def grow_and_round(self: GrowableT, ratio: float) -> GrowableT:
        """Multiplies this instance by ratio, rounding."""
