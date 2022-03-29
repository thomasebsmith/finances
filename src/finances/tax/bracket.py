from __future__ import annotations

from dataclasses import dataclass

from ..earnings import Earnings
from ..money import Money, ZERO

@dataclass
class Bracket:
    marginal_rate: float
    threshold: Money

class BracketTax:
    def __init__(self, brackets: list[Bracket]):
        self.brackets = sorted(
            brackets,
            key=lambda b: b.threshold,
            reverse=True
        )

    def calculate(self, earnings: Earnings) -> Money:
        tax = ZERO
        agi = earnings.agi()
        for bracket in self.brackets:
            if agi > bracket.threshold:
                tax += (
                    agi - bracket.threshold
                ).grow_and_round(bracket.marginal_rate)
                agi = bracket.threshold
        return tax
