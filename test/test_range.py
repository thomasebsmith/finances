"""Tests of src/finances/utilities/range.py."""

from pytest import raises

from finances import Money
from finances.utilities import Range


def test_create() -> None:
    """Tests creating a Range."""
    assert Range(0, 0).start == 0
    assert Range(0, 0).end == 0
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


def test_create_exception() -> None:
    """Tests creating invalid Ranges."""
    with raises(ValueError):
        Range(0, -1)
    with raises(ValueError):
        Range(8888888, 0)
    with raises(ValueError):
        Range(Money.of(32, 7), Money.of(3, 28))


def test_contains() -> None:
    """Tests the behavior of Range.contains."""
    assert Range(0, 1).contains(0)
    assert not Range(0, 1).contains(1)
    assert not Range(0, 1).contains(-1)
    assert not Range(0, 0).contains(0)
    assert not Range(0, 0).contains(5)
    assert Range(Range.NEGATIVE_INFINITY, 0).contains(-5)
    assert not Range(Range.NEGATIVE_INFINITY, 0).contains(0)
    assert not Range(Range.NEGATIVE_INFINITY, 0).contains(5)
    assert Range(-1, Range.POSITIVE_INFINITY).contains(-1)
    assert Range(-1, Range.POSITIVE_INFINITY).contains(987)
    assert not Range(-1, Range.POSITIVE_INFINITY).contains(-2)
    assert Range[int](
        Range.NEGATIVE_INFINITY, Range.POSITIVE_INFINITY
    ).contains(-100)
    assert Range[int](
        Range.NEGATIVE_INFINITY, Range.POSITIVE_INFINITY
    ).contains(0)
    assert Range[int](
        Range.NEGATIVE_INFINITY, Range.POSITIVE_INFINITY
    ).contains(987)
    assert Range(Money.of(31, 41), Money.of(159, 26)).contains(Money.of(62, 83))
    assert not Range(Money.of(31, 41), Money.of(159, 26)).contains(
        Money.of(2997924, 58)
    )


def test_surrounds() -> None:
    """Tests the behavior of Range.surrounds."""
    assert Range(5, 5).surrounds(Range(5, 5))
    assert not Range(Money.of(-1), Money.of(-1)).surrounds(
        Range(Money.of(-1), Money.of(0))
    )
    assert Range(8.2, 9.3).surrounds(Range(8.2, 9.2))
    assert Range(10, 20).surrounds(Range(15, 20))
    assert Range(Range.NEGATIVE_INFINITY, 0).surrounds(Range(-5, -3))
    assert Range(20, Range.POSITIVE_INFINITY).surrounds(Range(20, 25))
    assert not Range(Range.NEGATIVE_INFINITY, 99).surrounds(Range(98, 100))
    assert not Range(0, Range.POSITIVE_INFINITY).surrounds(
        Range(Range.NEGATIVE_INFINITY, 0)
    )
    assert Range(Range.NEGATIVE_INFINITY, Range.POSITIVE_INFINITY).surrounds(
        Range(Range.NEGATIVE_INFINITY, Range.POSITIVE_INFINITY)
    )
    assert Range[int](
        Range.NEGATIVE_INFINITY, Range.POSITIVE_INFINITY
    ).surrounds(Range(-99, 109))
