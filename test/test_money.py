"""Tests of src/finances/money.py."""

from finances import Money
from finances.money import ZERO


def test_of():
    """Tests the behavior of Money.of."""
    assert Money.of(0) == ZERO
    assert Money.of(98765) == Money(9876500)
    assert Money.of(-123) == Money(-12300)
    assert Money.of(0, 0) == ZERO
    assert Money.of(8765, 30) == Money(876530)
    assert Money.of(-314, 15) == Money(-31415)
