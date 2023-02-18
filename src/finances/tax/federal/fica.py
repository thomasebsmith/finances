"""Contains classes and utilities related to FICA taxes."""

from ...earnings import EarningsTaxPolicy, EarningsType, TaxCategory
from ...money import Money
from ..composite import CompositeTax
from ..bracket import Bracket, BracketTax
from ..flat import FlatTax
from .data import (
    ADDITIONAL_MEDICARE_TAX_RATE,
    ADDITIONAL_MEDICARE_TAX_THRESHOLDS,
    MEDICARE_TAX_DATA_YEARS,
    MEDICARE_TAX_RATE,
    SOCIAL_SECURITY_TAX_RATE,
    WAGE_BASE_LIMIT_BY_YEAR,
)
from .status import FilingStatus


class SocialSecurityTax(FlatTax):
    """The United States federal social security tax."""

    def __init__(self, year: int):
        """
        Creates a SocialSecurityTax.

        Arguments:
            year - The tax year.
        """
        assert (
            year in WAGE_BASE_LIMIT_BY_YEAR
        ), f"no social security tax data for {year}"
        super().__init__(
            SOCIAL_SECURITY_TAX_RATE,
            EarningsTaxPolicy(
                earnings_type=EarningsType.GROSS_INCOME,
                category=TaxCategory.FEDERAL,
                ceiling=WAGE_BASE_LIMIT_BY_YEAR[year],
            ),
        )


class MedicareTax(BracketTax):
    """
    The United States federal medicare tax.

    Includes additional medicare tax.
    """

    def __init__(self, year: int, filing_status: FilingStatus):
        """
        Creates a MedicareTax.

        Arguments:
            year - The tax year.
            filing_status - The filing status of the taxpayer.
        """
        assert (
            year in MEDICARE_TAX_DATA_YEARS
        ), f"no medicare tax data for {year}"
        super().__init__(
            [
                Bracket(
                    MEDICARE_TAX_RATE + ADDITIONAL_MEDICARE_TAX_RATE,
                    ADDITIONAL_MEDICARE_TAX_THRESHOLDS[filing_status],
                ),
                Bracket(MEDICARE_TAX_RATE, Money.of(0)),
            ],
            policy=EarningsTaxPolicy(
                earnings_type=EarningsType.GROSS_INCOME,
                category=TaxCategory.FEDERAL,
            ),
        )


class FICATax(CompositeTax):
    """United States FICA taxes (social security and medicare combined)."""

    def __init__(self, year: int, filing_status: FilingStatus):
        """
        Creates a FICATax.

        Arguments:
            year - The tax year.
            filing_status - The filing status of the tax payer.
        """
        super().__init__(
            [
                SocialSecurityTax(year),
                MedicareTax(year, filing_status),
            ]
        )
