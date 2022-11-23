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


def test_near() -> None:
    """Tests the behavior of Range.near."""

    def expect_near(range1: Range[int], range2: Range[int]) -> None:
        assert range1.near(range2)
        assert range2.near(range1)

    def expect_not_near(range1: Range[int], range2: Range[int]) -> None:
        assert not range1.near(range2)
        assert not range2.near(range1)

    expect_near(Range(0, 0), Range(0, 0))
    expect_near(Range(0, 0), Range(0, 5))
    expect_near(Range(0, 0), Range(-5, 0))
    expect_not_near(Range(0, 0), Range(1, 1))
    expect_not_near(Range(0, 0), Range(1, 5))
    expect_not_near(Range(0, 0), Range(-5, -1))

    expect_near(Range(1, 3), Range(2, 4))
    expect_near(Range(1, 4), Range(-1, 3))
    expect_near(Range(2, 5), Range(1, 5))
    expect_near(Range(2, 5), Range(1, 6))
    expect_near(Range(2, 5), Range(2, 6))

    expect_near(
        Range(Range.NEGATIVE_INFINITY, 0),
        Range(0, Range.POSITIVE_INFINITY),
    )
    expect_near(
        Range(Range.NEGATIVE_INFINITY, 0),
        Range(0, 5),
    )
    expect_near(
        Range(Range.NEGATIVE_INFINITY, 0),
        Range(-1, 0),
    )
    expect_near(
        Range(Range.NEGATIVE_INFINITY, 0),
        Range(-1, -1),
    )
    expect_near(
        Range(Range.NEGATIVE_INFINITY, 0),
        Range(-5, -3),
    )
    expect_not_near(
        Range(Range.NEGATIVE_INFINITY, 0),
        Range(1, 5),
    )
    expect_near(
        Range(5, Range.POSITIVE_INFINITY),
        Range(1, 6),
    )
    expect_near(
        Range(5, Range.POSITIVE_INFINITY),
        Range(8, Range.POSITIVE_INFINITY),
    )
    expect_near(
        Range(5, Range.POSITIVE_INFINITY),
        Range(8, Range.POSITIVE_INFINITY),
    )
    expect_near(Range(5, Range.POSITIVE_INFINITY), Range(0, 5))
    expect_not_near(Range(5, Range.POSITIVE_INFINITY), Range(-88, -88))
