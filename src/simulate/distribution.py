"""Types and functions for dealing with numeric distributions."""
from typing import Generic, Protocol, TypeVar

from finances import AddableComparable, Range


_RangeT_contra = TypeVar(
    "_RangeT_contra", bound=AddableComparable, contravariant=True
)
_ValueT_co = TypeVar("_ValueT_co", bound=AddableComparable, covariant=True)


class Distribution(Protocol, Generic[_RangeT_contra, _ValueT_co]):
    """A type that stores numeric distributions."""

    def average(self, in_range: Range[_RangeT_contra]) -> _ValueT_co:
        """Returns the average value in the given range."""
