#!/usr/bin/env python3

import sys

from .earnings import Earnings
from .money import Money, ZERO

def main():
    income = Earnings(gross_income=Money(5000000), deductions=ZERO)
    print(income.agi())
    return 0

if __name__ == "__main__":
    sys.exit(main())
