"""Tests of src/simulate/growth.py."""

from finances import Money
from simulate.growth import accumulate_and_grow, grow


def test_accumulate_and_grow() -> None:
    """Tests the behavior of accumulate_and_grow."""
    assert accumulate_and_grow(Money.ZERO, 1.0, 0) == Money.ZERO
    assert accumulate_and_grow(Money.ZERO, 1.0, 10) == Money.ZERO
    assert accumulate_and_grow(Money.of(10), 1.0, 5) == Money.of(50)

    assert accumulate_and_grow(Money.of(7, 11), 2.35, 10) == Money.of(42736, 8)
    assert accumulate_and_grow(Money.of(314), 0.11, 8) == Money.of(142, 26)
    assert accumulate_and_grow(Money.of(-1, 99), 10.01, 2) == Money.of(-85, 70)
    assert accumulate_and_grow(Money.of(-25, 9), 0.9, 22) == Money.of(-214, 68)


def test_grow() -> None:
    """Tests the behavior of grow."""
    assert grow(Money.ZERO, 0.01, 0) == Money.ZERO
    assert grow(Money.ZERO, 123.456, 78) == Money.ZERO
    assert grow(Money.ZERO, 987.6, -5) == Money.ZERO

    assert grow(Money.of(22, 33), 1.0, 100) == Money.of(22, 33)
    assert grow(Money.of(-66, 55), 1.0, -98) == Money.of(-66, 55)

    assert grow(Money.of(12, 45), 1.5, 9) == Money.of(478, 62)
    assert grow(Money.of(-6, 55), 0.5, 3) == Money.of(Money.NEGATIVE_ZERO, 82)
