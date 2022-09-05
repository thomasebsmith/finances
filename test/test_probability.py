"""Tests of src/simulate/probability.py."""

from fractions import Fraction

from simulate.probability import Probability


def test_value() -> None:
    """Tests the behavior of Probability.value."""
    assert Probability.ZERO.value() == Fraction(0)
    assert Probability.ONE.value() == Fraction(1)
    assert Probability(Fraction(3, 5)).value() == Fraction(3, 5)
    assert Probability(Fraction(2, 7)).value() == Fraction(2, 7)
    assert Probability(Fraction(10, 11)).value() == Fraction(10, 11)
    assert Probability(Fraction(1, 2)).value() == Fraction(1, 2)


def test_add() -> None:
    """Tests the behavior of Probability.__add__."""
    assert Probability.ZERO + Probability.ONE == Probability.ONE
    assert Probability.ONE + Probability.ZERO == Probability.ONE
    assert Probability(Fraction(0)) + Probability.ZERO == Probability.ZERO
    assert Probability(Fraction(1, 2)) + Probability(
        Fraction(1, 2)
    ) == Probability(Fraction(1))
    assert Probability(Fraction(8, 65)) + Probability(
        Fraction(29, 39)
    ) == Probability(Fraction(169, 195))
    assert Probability(Fraction(1, 100)) + Probability(
        Fraction(2, 25)
    ) == Probability(Fraction(9, 100))


def test_multiply() -> None:
    """Tests the behavior of Probability.__mul__."""
    assert Probability.ZERO * Probability.ZERO == Probability.ZERO
    assert Probability.ONE * Probability.ONE == Probability.ONE
    assert Probability.ZERO * Probability.ONE == Probability.ZERO
    assert Probability.ONE * Probability.ZERO == Probability.ZERO
    assert Probability(Fraction(1, 2)) * Probability.ONE == Probability(
        Fraction(1, 2)
    )
    assert Probability(Fraction(3, 7)) * Probability(
        Fraction(88, 89)
    ) == Probability(Fraction(264, 623))
    assert Probability(Fraction(21, 24)) * Probability(
        Fraction(15, 29)
    ) == Probability(Fraction(105, 232))
