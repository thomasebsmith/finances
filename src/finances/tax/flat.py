"""Contains classes and utilities related to fixed-percentage taxes."""

from ..earnings import Earnings, EarningsTaxPolicy
from ..money import Money

class FlatTax:
    """A fixed-percentage tax on income."""

    def __init__(self, rate: float, policy: EarningsTaxPolicy):
        """
        Creates a FlatTax at the given rate with the given policy.

        Arguments:
            rate - The tax rate, usually between 0 and 1.
            policy - The policy to use to determine taxable income.
        """
        self.rate = rate
        self.policy = policy

    def calculate(self, earnings: Earnings) -> Money:
        """
        Calculates the amount of tax to be levied on earnings.

        Arguments:
            earnings - The earnings to tax.
        Return value: (earnings's taxable income) * (the flat tax rate).
        """
        return (earnings
                .taxable_income(self.policy)
                .grow_and_round(self.rate))
