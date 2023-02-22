"""Tests of src/finances/earnings.py."""

from finances import (
    Earnings,
    EarningsTaxPolicy,
    EarningsType,
    Money,
    TaxCategory,
)


EARNINGS_1 = Earnings(
    gross_income=Money.of(100000),
    adjustments={
        TaxCategory.FEDERAL: Money.of(100),
        TaxCategory.STATE: Money.of(200),
        TaxCategory.LOCAL: Money.of(300),
    },
    deductions={
        TaxCategory.FEDERAL: Money.of(9000),
        TaxCategory.STATE: Money.of(8000),
        TaxCategory.LOCAL: Money.of(7000),
    },
    magi_additions={
        TaxCategory.FEDERAL: Money.of(10),
        TaxCategory.STATE: Money.of(20),
        TaxCategory.LOCAL: Money.of(30),
    },
)


TAX_POLICY_1 = EarningsTaxPolicy(
    earnings_type=EarningsType.AGI,
    category=TaxCategory.FEDERAL,
)


TAX_POLICY_2 = EarningsTaxPolicy(
    earnings_type=EarningsType.AGI_WITH_DEDUCTIONS,
    category=TaxCategory.STATE,
    floor=Money.of(92500),
)


TAX_POLICY_3 = EarningsTaxPolicy(
    earnings_type=EarningsType.AGI_WITH_DEDUCTIONS,
    category=TaxCategory.LOCAL,
    ceiling=Money.of(200000),
)

TAX_POLICY_4 = EarningsTaxPolicy(
    earnings_type=EarningsType.GROSS_INCOME,
    category=TaxCategory.FEDERAL,
    ceiling=Money.of(99999),
)

TAX_POLICY_5 = EarningsTaxPolicy(
    earnings_type=EarningsType.MAGI,
    category=TaxCategory.STATE,
)

TAX_POLICY_6 = EarningsTaxPolicy(
    earnings_type=EarningsType.AGI_WITH_DEDUCTIONS,
    category=TaxCategory.STATE,
    floor=Money.of(1),
)


def test_agi() -> None:
    """Tests the behavior of Earnings.agi."""
    assert EARNINGS_1.agi(TaxCategory.FEDERAL) == Money.of(99900)
    assert EARNINGS_1.agi(TaxCategory.STATE) == Money.of(99800)
    assert EARNINGS_1.agi(TaxCategory.LOCAL) == Money.of(99700)


def test_magi() -> None:
    """Tests the behavior of Earnings.magi."""
    assert EARNINGS_1.magi(TaxCategory.FEDERAL) == Money.of(99910)
    assert EARNINGS_1.magi(TaxCategory.STATE) == Money.of(99820)
    assert EARNINGS_1.magi(TaxCategory.LOCAL) == Money.of(99730)


def test_taxable_income() -> None:
    """Tests the behavior of Earnings.taxable_income."""
    assert EARNINGS_1.taxable_income(TAX_POLICY_1) == Money.of(99900)
    assert EARNINGS_1.taxable_income(TAX_POLICY_2) == Money.of(92500)
    assert EARNINGS_1.taxable_income(TAX_POLICY_3) == Money.of(92700)
    assert EARNINGS_1.taxable_income(TAX_POLICY_4) == Money.of(99999)
    assert EARNINGS_1.taxable_income(TAX_POLICY_5) == Money.of(99820)
    assert EARNINGS_1.taxable_income(TAX_POLICY_6) == Money.of(91800)
