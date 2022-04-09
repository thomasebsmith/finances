"""Classes and utilities related to combining taxes."""

from __future__ import annotations

from ..earnings import Earnings
from ..money import Money, ZERO
from .tax import IncomeTax

class CompositeTax:
    """An income tax that is calculated as the sum of 0 or more other taxes."""

    def __init__(self, taxes: list[IncomeTax]):
        """
        Creates a CompositeTax.

        Arguments:
            taxes - The taxes to sum in order to levy this tax.
        """
        self.taxes = taxes

    def calculate(self, earnings: Earnings) -> Money:
        """
        Calculates the amount of tax to be levied on earnings.

        Arguments:
            earnings - The earnings to tax.
        Return value: The sum of all of self.taxes levied on earnings.
        """
        return sum((tax.calculate(earnings) for tax in self.taxes), start=ZERO)
