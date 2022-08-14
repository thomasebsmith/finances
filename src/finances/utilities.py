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
