from __future__ import annotations

from dataclasses import dataclass

from ..earnings import Earnings, EarningsTaxPolicy
from ..money import Money, ZERO

@dataclass
class Bracket:
    marginal_rate: float
    threshold: Money

class BracketTax:
    def __init__(self, brackets: list[Bracket], policy: EarningsTaxPolicy):
        self.brackets = sorted(
            brackets,
            key=lambda b: b.threshold,
            reverse=True
        )
        self.policy = policy

    def calculate(self, earnings: Earnings) -> Money:
        tax = ZERO
        taxable_income = earnings.taxable_income(self.policy)
        for bracket in self.brackets:
            if taxable_income > bracket.threshold:
                tax += (
                    taxable_income - bracket.threshold
                ).grow_and_round(bracket.marginal_rate)
                taxable_income = bracket.threshold
        return tax
