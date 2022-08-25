"""Utility classes and functions that are not directly related to finances."""
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
