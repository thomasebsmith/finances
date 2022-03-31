from __future__ import annotations

from dataclasses import dataclass

from ..earnings import Earnings
from ..money import Money
from .tax import IncomeTax

class CompositeTax:
    def __init__(self, taxes: list[IncomeTax]):
        self.taxes = taxes

    def calculate(self, earnings: Earnings) -> Money:
        return sum((tax.calculate(earnings) for tax in self.taxes))
