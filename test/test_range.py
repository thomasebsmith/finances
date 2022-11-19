"""Tests of src/finances/utilities/range.py."""

from finances import Money
from finances.utilities import Range


def test_create() -> None:
    """Tests creating a Range."""
    assert Range(3, 5).start == 3
    assert Range(3, 5).end == 5
    assert Range(Money.of(-5), Money.of(100, 34)).start == Money.of(-5)
    assert Range(Money.of(-5), Money.of(100, 34)).end == Money.of(100, 34)
    assert Range(Range.NEGATIVE_INFINITY, -5).start == Range.NEGATIVE_INFINITY
    assert Range(Range.NEGATIVE_INFINITY, -5).end == -5
    assert Range(987.6, Range.POSITIVE_INFINITY).start == 987.6
    assert Range(987.6, Range.POSITIVE_INFINITY).end == Range.POSITIVE_INFINITY
    assert (
        Range(Range.NEGATIVE_INFINITY, Range.POSITIVE_INFINITY).start
        == Range.NEGATIVE_INFINITY
    )
    assert (
        Range(Range.NEGATIVE_INFINITY, Range.POSITIVE_INFINITY).end
        == Range.POSITIVE_INFINITY
    )
