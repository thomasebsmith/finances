from __future__ import annotations

from dataclasses import dataclass

from ..earnings import Earnings
from ..money import Money, ZERO

@dataclass
class Bracket:
    marginal_rate: float
    threshold: Money

class BracketTax:
    def __init__(self, brackets: list[Bracket], allow_deductions: bool):
        self.allow_deductions = allow_deductions
        self.brackets = sorted(
            brackets,
            key=lambda b: b.threshold,
            reverse=True
        )

    def calculate(self, earnings: Earnings) -> Money:
        tax = ZERO
        taxable_income = earnings.taxable_income(self.allow_deductions)
        for bracket in self.brackets:
            if taxable_income > bracket.threshold:
                tax += (
                    taxable_income - bracket.threshold
                ).grow_and_round(bracket.marginal_rate)
                taxable_income = bracket.threshold
        return tax
