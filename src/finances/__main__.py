#!/usr/bin/env python3

"""An example script that uses this module to calculate income tax."""

import sys

from .earnings import Earnings, TaxCategory
from .money import Money, ZERO
from .tax import FederalIncomeTax, FICATax, FilingStatus
from .tax.state.mi import MichiganIncomeTax


def print_taxes(
    gross_income: Money,
    year: int,
    deductions: Money,
    personal_exemption: Money,
):
    """
    Prints the taxes required for a single person's income.

    Assumes that no extra deductions or exemptions are available, and that the
    person lives in Michigan.

    Arguments:
        gross_income - The person's gross income for the year.
        year - The tax year.
        deductions - The deductions for the year.
        personal_exemption - The Michigan personal exemption for the year.
    """
    fed_income_tax = FederalIncomeTax(year, FilingStatus.SINGLE)
    mi_income_tax = MichiganIncomeTax(year)
    fica = FICATax(year, FilingStatus.SINGLE)
    income = Earnings(
        gross_income=gross_income,
        deductions={
            TaxCategory.FEDERAL: deductions,
            TaxCategory.STATE: personal_exemption,
        },
        magi_additions={
            TaxCategory.FEDERAL: ZERO,
            TaxCategory.STATE: ZERO,
        },
    )
    taxes = sum(
        [
            fed_income_tax.calculate(income),
            mi_income_tax.calculate(income),
            fica.calculate(income),
        ],
        start=ZERO,
    )
    print(f"{year} taxes on {gross_income}: {taxes}")


def main():
    """Prints the amount of federal taxes on $100,000 in 2021 and 2022."""
    gross_income = Money.parse(input("Gross income: "))
    deductions = Money.parse(input("Itemized deductions: "))
    print_taxes(
        gross_income, 2021, max(deductions, Money.of(12550)), Money.of(4900)
    )
    print_taxes(
        gross_income, 2022, max(deductions, Money.of(12950)), Money.of(5000)
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
