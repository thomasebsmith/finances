from dataclasses import dataclass
from typing import Optional

from .money import Money

@dataclass(frozen=True)
class EarningsTaxPolicy:
    allow_deductions: bool
    floor: Optional[Money] = None
    ceiling: Optional[Money] = None

    def __post_init__(self):
        if self.floor is not None and self.ceiling is not None:
            assert self.floor <= self.ceiling, "floor must not exceed ceiling"

@dataclass(frozen=True)
class Earnings:
    gross_income: Money
    deductions: Money

    def taxable_income(self, policy: EarningsTaxPolicy) -> Money:
        income = self.agi() if policy.allow_deductions else self.gross_income

        if policy.floor is not None:
            income = max(policy.floor, income)
        if policy.ceiling is not None:
            income = min(policy.ceiling, income)

        return income

    def agi(self) -> Money:
        return self.gross_income - self.deductions
