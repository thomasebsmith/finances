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
    """Tests the behavior of Distribution.__mul__."""
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


def test_subset() -> None:
    """Tests the behavior of Distribution.__getitem__(Range)."""
    dist = ConstantDistribution[float, int](26)
    subset = dist[Range(-100.5, 67.8)]
    assert subset.value(-100.5) == 26
    assert subset.value(67.7999) == 26
    assert subset[1.0] == 26
    assert subset.average(Range(-100.5, 67.8)) == 26
    assert subset.average(Range(64.1, 64.8)) == 26
    assert subset.range() == Range(-100.5, 67.8)


def test_defaulting_to() -> None:
    """Tests Distribution.defaulting_to."""
    dist = ConstantDistribution[int, int](0)
    subset = dist[Range(-15, -10)]
    defaulting = subset.defaulting_to(ConstantDistribution[int, int](5))
    assert defaulting.value(-15) == 0
    assert defaulting[-13] == 0
    assert defaulting[-10] == 5
    assert defaulting.value(300) == 5
    assert defaulting.range() == Range[int](
        Range.NEGATIVE_INFINITY, Range.POSITIVE_INFINITY
    )


def test_combinations() -> None:
    """Tests the combined behavior of Distribution methods."""
    dist = ConstantDistribution[float, int](314159)
    dist2 = ConstantDistribution[float, int](-105000)
    combo = dist + dist2[Range(3.14, 6.28)] * 2
    assert combo.value(3.14) == 104159
    assert combo.value(6.27) == 104159
    assert combo[4.0] == 104159
    assert combo.average(Range(3.14, 6.28)) == 104159
    assert combo.average(Range(4.0, 5.0)) == 104159
    assert combo.range() == Range(3.14, 6.28)
