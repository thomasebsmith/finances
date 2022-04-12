#!/usr/bin/env python3

"""An example script that uses this module to calculate income tax."""

import sys

from .earnings import Earnings, TaxCategory
from .money import Money, ZERO
from .tax import FederalIncomeTax, FICATax, FilingStatus
from .tax.state.mi import MichiganIncomeTax


def print_taxes(
    year: int, standard_deduction: Money, personal_exemption: Money
):
    """
    Prints the taxes required for $100,000 of a single person's income.

    Assumes that no extra deductions or exemptions are available, and that the
    person lives in Michigan.

    Arguments:
        year - The tax year.
        standard_deduction - The U.S. federal standard deduction for the year.
        personal_exemption - The Michigan personal exemption for the year.
    """
    gross_income = Money.of(100000)
    fed_income_tax = FederalIncomeTax(year, FilingStatus.SINGLE)
    mi_income_tax = MichiganIncomeTax(year)
    fica = FICATax(year, FilingStatus.SINGLE)
    income = Earnings(
        gross_income=gross_income,
        deductions={
            TaxCategory.FEDERAL: standard_deduction,
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
    print_taxes(2021, Money.of(12550), Money.of(4900))
    print_taxes(2022, Money.of(12950), Money.of(5000))
    return 0


if __name__ == "__main__":
    sys.exit(main())
