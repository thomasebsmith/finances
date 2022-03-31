#!/usr/bin/env python3

import sys

from .earnings import Earnings, EarningsTaxPolicy
from .money import Money, ZERO
from .tax import FederalIncomeTax, FilingStatus

def main():
    income_tax = FederalIncomeTax(2021, FilingStatus.SINGLE)
    income = Earnings(
        gross_income=Money.of(100000),
        deductions=Money.of(12550),
        magi_additions=ZERO
    )
    print(income_tax.calculate(income))
    return 0

if __name__ == "__main__":
    sys.exit(main())
