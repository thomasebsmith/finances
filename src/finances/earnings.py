from dataclasses import dataclass

from .money import Money

@dataclass(frozen=True)
class Earnings:
    gross_income: Money
    deductions: Money

    def taxable_income(self, allow_deductions: bool) -> Money:
        return self.agi() if allow_deductions else self.gross_income

    def agi(self) -> Money:
        return self.gross_income - self.deductions
