"""Tests of src/finances/money.py."""

from finances import Money
from finances.money import ZERO, NEGATIVE_ZERO


def test_of():
    """Tests the behavior of Money.of."""
    assert Money.of(0) == ZERO
    assert Money.of(98765) == Money(9876500)
    assert Money.of(-123) == Money(-12300)
    assert Money.of(0, 0) == ZERO
    assert Money.of(8765, 30) == Money(876530)
    assert Money.of(-314, 15) == Money(-31415)
    assert Money.of(NEGATIVE_ZERO, 46) == Money(-46)


def test_parse():
    """Tests the behavior of Money.parse."""
    assert Money.parse("$100") == Money.of(100)
    assert Money.parse("$0.34") == Money.of(0, 34)
    assert Money.parse("$0") == ZERO
    assert Money.parse("-$0") == ZERO
    assert Money.parse("-$923.60") == Money.of(-923, 60)


def test_truncated_dollars():
    """Tests the behavior of Money.truncated_dollars."""
    assert ZERO.truncated_dollars() == 0
    assert Money.of(0, 99).truncated_dollars() == 0
    assert Money.of(101, 1).truncated_dollars() == 101
    assert Money.of(57).truncated_dollars() == 57
    assert Money(-99).truncated_dollars() == 0
    assert Money.of(-1, 1).truncated_dollars() == -1
    assert Money.of(-85, 50).truncated_dollars() == -85


def test_extra_cents():
    """Tests the behavior of Money.extra_cents."""
    assert ZERO.extra_cents() == 0
    assert Money.of(0, 99).extra_cents() == 99
    assert Money.of(101, 1).extra_cents() == 1
    assert Money.of(57).extra_cents() == 0
    assert Money(-99).extra_cents() == 99
    assert Money.of(-1, 1).extra_cents() == 1
    assert Money.of(-85, 50).extra_cents() == 50
