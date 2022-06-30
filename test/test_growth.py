"""Tests of src/simulate/growth.py."""

from finances import Money
from simulate.growth import grow


def test_grow():
    """Tests the behavior of grow."""
    assert grow(Money.of(0), 0.01, 0) == Money.of(0)
    assert grow(Money.of(0), 123.456, 78) == Money.of(0)
    assert grow(Money.of(0), 987.6, -5) == Money.of(0)

    assert grow(Money.of(22, 33), 1.0, 100) == Money.of(22, 33)
    assert grow(Money.of(-66, 55), 1.0, -98) == Money.of(-66, 55)

    assert grow(Money.of(12, 45), 1.5, 9) == Money.of(478, 62)
