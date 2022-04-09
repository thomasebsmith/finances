"""Contains general tax utilities."""

from typing import Protocol

from ..earnings import Earnings
from ..money import Money

class IncomeTax(Protocol):
    """A tax on earnings."""
    def calculate(self, earnings: Earnings) -> Money:
        """Calculates the amount of tax to be levied on earnings."""
