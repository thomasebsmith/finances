"""Tests of src/simulate/distribution/*.py."""

from finances.utilities import Range
from simulate.distribution import ConstantDistribution


def test_constant_distribution() -> None:
    """Tests the behavior of ConstantDistribution."""
    dist = ConstantDistribution[int, float](3.14159)
    assert dist.value(-3) == 3.14159
    assert dist[9999999] == 3.14159
    assert dist.value(0) == 3.14159
    assert dist.average(Range(-1, 1)) == 3.14159
    assert (
        dist.average(Range(Range.NEGATIVE_INFINITY, Range.POSITIVE_INFINITY))
        == 3.14159
    )
    assert dist.average(Range(0, 0)) == 3.14159
    assert dist.range() == Range[int](
        Range.NEGATIVE_INFINITY, Range.POSITIVE_INFINITY
    )


def test_add() -> None:
    """Tests the behavior of Distribution.__add__."""
    dist1 = ConstantDistribution[int, int](-99)
    dist2 = ConstantDistribution[int, int](101)
    dist = dist1 + dist2
    assert dist[0] == 2
    assert dist.value(31415) == 2
    assert dist[-628] == 2
    assert dist.average(Range(-100, -3)) == 2
    assert dist.average(Range(0, Range.POSITIVE_INFINITY)) == 2
    assert dist.range() == Range[int](
        Range.NEGATIVE_INFINITY, Range.POSITIVE_INFINITY
    )


def test_mul() -> None:
    """Test the behavior of Distribution.__mul__."""
    dist = ConstantDistribution[int, int](-50)
    multiplied = dist * 7
    assert multiplied.value(-2) == -350
    assert multiplied.value(33333) == -350
    assert multiplied[987665] == -350
    assert multiplied.average(Range(500, 501)) == -350
    assert multiplied.average(Range(Range.NEGATIVE_INFINITY, -1)) == -350
    assert multiplied.range() == Range[int](
        Range.NEGATIVE_INFINITY, Range.POSITIVE_INFINITY
    )
