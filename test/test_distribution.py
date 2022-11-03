"""Tests of src/simulate/distribution/*.py."""

from finances.utilities import Range
from simulate.distribution import ConstantDistribution


def test_constant_distribution() -> None:
    """Tests the behavior of ConstantDistribution."""
    dist = ConstantDistribution[int, float](3.14159)
    assert dist.value(-3) == 3.14159
    assert dist.value(9999999) == 3.14159
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
