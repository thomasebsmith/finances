#!/usr/bin/env python3

"""An example script that uses this module to calculate income tax."""

import sys

from .earnings import Earnings, TaxCategory
from .money import Money, ZERO
from .tax import FederalIncomeTax, FICATax, FilingStatus
from .tax.state.mi import MichiganIncomeTax


def main():
    """Prints the amount of federal taxes on $100,000 in 2021."""
    fed_income_tax = FederalIncomeTax(2021, FilingStatus.SINGLE)
    mi_income_tax = MichiganIncomeTax(2021)
    fica = FICATax(2021, FilingStatus.SINGLE)
    income = Earnings(
        gross_income=Money.of(100000),
        deductions={
            TaxCategory.FEDERAL: Money.of(12550),
            TaxCategory.STATE: Money.of(4900),
        },
        magi_additions={
            TaxCategory.FEDERAL: ZERO,
            TaxCategory.STATE: ZERO,
        },
    )
    print(
        sum(
            [
                fed_income_tax.calculate(income),
                mi_income_tax.calculate(income),
                fica.calculate(income),
            ],
            start=ZERO,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
