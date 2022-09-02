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
