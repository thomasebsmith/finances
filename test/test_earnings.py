"""Tests of src/finances/earnings.py."""

from finances import Earnings, EarningsTaxPolicy, Money, TaxCategory


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


TAX_POLICY_1 = EarningsTaxPolicy(
    allow_deductions=False,
    category=TaxCategory.FEDERAL,
)


TAX_POLICY_2 = EarningsTaxPolicy(
    allow_deductions=True,
    category=TaxCategory.STATE,
    floor=Money.of(92500),
)


TAX_POLICY_3 = EarningsTaxPolicy(
    allow_deductions=True,
    category=TaxCategory.LOCAL,
    ceiling=Money.of(200000),
)


def test_agi() -> None:
    """Tests the behavior of Earnings.agi."""
    # Note: This test is incorrect. It does not correctly distinguish between
    # deductions from gross income and deductions from AGI.
    assert EARNINGS_1.agi(TaxCategory.FEDERAL) == Money.of(91000)
    assert EARNINGS_1.agi(TaxCategory.STATE) == Money.of(92000)
    assert EARNINGS_1.agi(TaxCategory.LOCAL) == Money.of(93000)


def test_magi() -> None:
    """Tests the behavior of Earnings.magi."""
    # Note: This test is incorrect. It does not correctly distinguish between
    # deductions from gross income and deductions from AGI.
    assert EARNINGS_1.magi(TaxCategory.FEDERAL) == Money.of(91100)
    assert EARNINGS_1.magi(TaxCategory.STATE) == Money.of(92200)
    assert EARNINGS_1.magi(TaxCategory.LOCAL) == Money.of(93300)


def test_taxable_income() -> None:
    """Tests the behavior of Earnings.taxable_income."""
    assert EARNINGS_1.taxable_income(TAX_POLICY_1) == Money.of(100000)
    assert EARNINGS_1.taxable_income(TAX_POLICY_2) == Money.of(92500)
    assert EARNINGS_1.taxable_income(TAX_POLICY_3) == Money.of(93000)
