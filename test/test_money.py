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


def test_all_cents():
    """Tests the behavior of Money.all_cents."""
    assert ZERO.all_cents() == 0
    assert Money.of(0, 51).all_cents() == 51
    assert Money.of(314, 5).all_cents() == 31405
    assert Money.of(-82).all_cents() == -8200
    assert Money.of(-1, 35).all_cents() == -135
    assert Money.of(NEGATIVE_ZERO, 68).all_cents() == -68
    assert Money.of(-62, 8).all_cents() == -6208


def test_str():
    """Tests the behavior of Money.__str__."""
    assert str(ZERO) == "$0.00"
    assert str(Money.of(0, 1)) == "$0.01"
    assert str(Money.of(3, 14)) == "$3.14"
    assert str(Money.of(27, 18)) == "$27.18"
    assert str(Money.of(NEGATIVE_ZERO, 35)) == "-$0.35"
    assert str(Money.of(-82, 6)) == "-$82.06"


def test_add():
    """Tests the behavior of Money.__add__."""
    assert ZERO + Money.of(0) == ZERO
    assert ZERO + Money.of(314, 15) == Money.of(314, 15)
    assert Money.of(-19, 2) + Money.of(0) == Money.of(-19, 2)
    assert Money.of(10) + Money.of(-10) == Money.of(0)
    assert Money.of(31, 15) + Money.of(-28, 26) == Money.of(2, 89)
    assert Money.of(8, 11) + Money.of(-20) == Money.of(-11, 89)


def test_sub():
    """Tests the behavior of Money.__sub__."""
    assert Money.of(0) - ZERO == ZERO
    assert Money.of(6, 28) - Money.of(0) == Money.of(6, 28)
    assert Money.of(-18, 25) - Money.of(-18, 25) == Money.of(0)
    assert Money.of(29, 37) - Money.of(28, 1) == Money.of(1, 36)
    assert Money.of(5, 90) - Money.of(101) == Money.of(-95, 10)
    assert Money.of(-20, 10) - Money.of(-30, 50) == Money.of(10, 40)
    assert Money.of(-60, 22) - Money.of(10, 23) == Money.of(-70, 45)


def test_mul():
    """Tests the behavior of Money.__mul__."""
    assert ZERO * 0 == ZERO
    assert Money.of(268, 11) * 0 == ZERO
    assert Money.of(-1) * 0 == ZERO
    assert ZERO * -1 == ZERO
    assert Money.of(-314, 25) * 1 == Money.of(-314, 25)
    assert Money.of(82, 22) * -1 == Money.of(-82, 22)
    assert Money.of(-165, 40) * -3 == Money.of(496, 20)
    assert Money.of(28, 37) * 22 == Money.of(624, 14)


def test_grow_and_round():
    """Tests the behavior of Money.grow_and_round."""
    assert ZERO.grow_and_round(0.0) == ZERO
    assert ZERO.grow_and_round(1.0) == Money.of(0)
    assert Money.of(123).grow_and_round(0.0) == ZERO
    assert Money.of(-9, 87).grow_and_round(0.0) == ZERO
    assert Money.of(1000, 0).grow_and_round(1.5) == Money.of(1500)
    assert Money.of(-953, 66).grow_and_round(0.782) == Money.of(-745, 76)
    assert Money.of(22000, 78).grow_and_round(12345.6789) == Money.of(
        271614565, 43
    )
