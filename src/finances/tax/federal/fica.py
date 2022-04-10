"""Contains classes and utilities related to FICA taxes."""

from __future__ import annotations

from ...earnings import Earnings, EarningsTaxPolicy, TaxCategory
from ...money import Money
from ..composite import CompositeTax
from ..bracket import Bracket, BracketTax
from ..flat import FlatTax
from .status import FilingStatus

WAGE_BASE_LIMIT_BY_YEAR = {2021: Money.of(142800, 0)}


class SocialSecurityTax:
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
        self._underlying = FlatTax(
            0.062,
            EarningsTaxPolicy(
                allow_deductions=False,
                category=TaxCategory.FEDERAL,
                ceiling=WAGE_BASE_LIMIT_BY_YEAR[year],
            ),
        )

    def calculate(self, earnings: Earnings) -> Money:
        """
        Calculates the amount of tax to be levied on earnings.

        Arguments:
            earnings - The earnings to tax.
        Return value: The amount of social security tax due.
        """
        return self._underlying.calculate(earnings)


AMT_THRESHOLDS: dict[FilingStatus, Money] = {
    FilingStatus.MARRIED_FILING_JOINTLY: Money.of(250000),
    FilingStatus.MARRIED_FILING_SEPARATELY: Money.of(125000),
    **dict.fromkeys(
        [
            FilingStatus.SINGLE,
            FilingStatus.HEAD_OF_HOUSEHOLD,
            FilingStatus.SURVIVING_SPOUSE,
        ],
        Money.of(200000),
    ),
}


class MedicareTax:
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
        assert year == 2021, f"no medicare tax data for {year}"
        self._underlying = BracketTax(
            [
                Bracket(0.0145 + 0.009, AMT_THRESHOLDS[filing_status]),
                Bracket(0.0145, Money.of(0)),
            ],
            policy=EarningsTaxPolicy(
                allow_deductions=False, category=TaxCategory.FEDERAL
            ),
        )

    def calculate(self, earnings: Earnings) -> Money:
        """
        Calculates the amount of tax to be levied on earnings.

        Arguments:
            earnings - The earnings to tax.
        Return value: The amount of medicare tax due.
        """
        return self._underlying.calculate(earnings)


class FICATax:
    """United States FICA taxes (social security and medicare combined)."""

    def __init__(self, year: int, filing_status: FilingStatus):
        """
        Creates a FICATax.

        Arguments:
            year - The tax year.
            filing_status - The filing status of the tax payer.
        """
        self._underlying = CompositeTax(
            [
                SocialSecurityTax(year),
                MedicareTax(year, filing_status),
            ]
        )

    def calculate(self, earnings: Earnings) -> Money:
        """
        Calculates the amount of tax to be levied on earnings.

        Arguments:
            earnings - The earnings to tax.
        Return value: The amount of FICA taxes due.
        """
        return self._underlying.calculate(earnings)
