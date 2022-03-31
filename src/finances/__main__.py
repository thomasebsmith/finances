#!/usr/bin/env python3

import sys

from .earnings import Earnings, EarningsTaxPolicy
from .money import Money
from .tax import Bracket, BracketTax

def main():
    bt = BracketTax([
        Bracket(0.37, Money.of(523600)),
        Bracket(0.35, Money.of(209425)),
        Bracket(0.32, Money.of(164925)),
        Bracket(0.24,  Money.of(86375)),
        Bracket(0.22,  Money.of(40525)),
        Bracket(0.12,   Money.of(9950)),
        Bracket(0.10,      Money.of(0)),
    ], policy=EarningsTaxPolicy(allow_deductions=True))
    income = Earnings(gross_income=Money.of(100000), deductions=Money.of(12550))
    print(bt.calculate(income))
    return 0

if __name__ == "__main__":
    sys.exit(main())
