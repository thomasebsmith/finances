from dataclasses import dataclass

from ..earnings import Earnings
from ..money import Money

class FlatTax:
    def __init__(self, rate: float, allow_deductions: bool):
        self.rate = rate
        self.allow_deductions = allow_deductions

    def calculate(self, earnings: Earnings) -> Money:
        return (earnings
                .taxable_income(self.allow_deductions)
                .grow_and_round(self.rate))
