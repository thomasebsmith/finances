from dataclasses import dataclass

from .money import Money

@dataclass(frozen=True)
class Earnings:
    gross_income: Money
    deductions: Money

    def agi(self) -> Money:
        return self.gross_income - self.deductions
