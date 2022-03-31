from dataclasses import dataclass

from ..earnings import Earnings, EarningsTaxPolicy
from ..money import Money

class FlatTax:
    def __init__(self, rate: float, policy: EarningsTaxPolicy):
        self.rate = rate
        self.policy = policy

    def calculate(self, earnings: Earnings) -> Money:
        return (earnings
                .taxable_income(self.policy)
                .grow_and_round(self.rate))
