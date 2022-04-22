"""Tests of src/finances/earnings.py."""

from finances import Earnings, Money, TaxCategory


EARNINGS_1 = Earnings(
    gross_income=Money.of(100000),
    deductions={
        TaxCategory.FEDERAL: Money.of(9000),
        TaxCategory.STATE: Money.of(8000),
        TaxCategory.LOCAL: Money.of(7000),
    },
    magi_additions={
        TaxCategory.FEDERAL: Money.of(100),
        TaxCategory.STATE: Money.of(200),
        TaxCategory.LOCAL: Money.of(300),
    },
)


def test_agi():
    """Tests the behavior of Earnings.agi."""
    assert EARNINGS_1.agi(TaxCategory.FEDERAL) == Money.of(91000)
    assert EARNINGS_1.agi(TaxCategory.STATE) == Money.of(92000)
    assert EARNINGS_1.agi(TaxCategory.LOCAL) == Money.of(93000)


def test_magi():
    """Tests the behavior of Earnings.magi."""
    assert EARNINGS_1.magi(TaxCategory.FEDERAL) == Money.of(91100)
    assert EARNINGS_1.magi(TaxCategory.STATE) == Money.of(92200)
    assert EARNINGS_1.magi(TaxCategory.LOCAL) == Money.of(93300)
