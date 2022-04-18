"""Classes and utilities related to taking the maximu of one or more taxes."""

from __future__ import annotations

from ..earnings import Earnings
from ..money import Money
from .tax import IncomeTax


class MaximumTax:
    """An income tax that is calculated as the highest of 1 or more taxes."""

    def __init__(self, taxes: list[IncomeTax]):
        """
        Creates a MaximumTax.

        Arguments:
            taxes - The taxes to sum in order to levy this tax.
        """
        assert len(taxes) > 0, "MaximumTax must be created with at least 1 tax"
        self.taxes = taxes

    def calculate(self, earnings: Earnings) -> Money:
        """
        Calculates the amount of tax to be levied on earnings.

        Arguments:
            earnings - The earnings to tax.
        Return value: The maximum of all of self.taxes levied on earnings.
        """
        return max((tax.calculate(earnings) for tax in self.taxes))
