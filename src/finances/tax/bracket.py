"""Contains classes and utilities related to bracket-based taxes."""

from __future__ import annotations

from dataclasses import dataclass

from ..earnings import Earnings, EarningsTaxPolicy
from ..money import Money, ZERO


@dataclass
class Bracket:
    """A tax bracket starting at threshold and continuing to higher incomes."""

    marginal_rate: float
    threshold: Money


class BracketTax:
    """A tax that has different fixed rates for different income buckets."""

    def __init__(self, brackets: list[Bracket], policy: EarningsTaxPolicy):
        """
        Creates a BracketTax.

        Arguments:
            brackets - The brackets to use to calculate this tax. Each
                threshold should be distinct.
            policy - The policy to use to determine taxable income.
        """

        def get_threshold(bracket: Bracket) -> Money:
            return bracket.threshold

        self.brackets = sorted(brackets, key=get_threshold, reverse=True)
        self.policy = policy

    def calculate(self, earnings: Earnings) -> Money:
        """
        Calculates the amount of tax to be levied on earnings.

        Arguments:
            earnings - The earnings to tax.
        Return value: The total tax, calculated by summing the amount of income
            in each tax bracket times that bracket's marginal_rate.
        """
        tax = ZERO
        taxable_income = earnings.taxable_income(self.policy)
        for bracket in self.brackets:
            if taxable_income > bracket.threshold:
                tax += (taxable_income - bracket.threshold).grow_and_round(
                    bracket.marginal_rate
                )
                taxable_income = bracket.threshold
        return tax
