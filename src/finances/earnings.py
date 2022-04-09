from __future__ import annotations

from dataclasses import dataclass
from enum import auto, Enum
from typing import Callable, Optional

from .money import Money, ZERO

class TaxCategory(Enum):
    FEDERAL = auto()
    STATE = auto()
    LOCAL = auto()

@dataclass(frozen=True)
class EarningsTaxPolicy:
    allow_deductions: bool
    category: TaxCategory
    floor: Optional[Money] = None
    ceiling: Optional[Money] = None

    def __post_init__(self):
        if self.floor is not None and self.ceiling is not None:
            assert self.floor <= self.ceiling, "floor must not exceed ceiling"

@dataclass(frozen=True)
class Earnings:
    gross_income: Money
    deductions: dict[TaxCategory, Money]
    magi_additions: dict[TaxCategory, Money]

    def taxable_income(self, policy: EarningsTaxPolicy) -> Money:
        income = (
            self.agi(policy.category) if policy.allow_deductions
            else self.gross_income
        )

        if policy.floor is not None:
            income = max(policy.floor, income)
        if policy.ceiling is not None:
            income = min(policy.ceiling, income)

        return income

    def agi(self, category: TaxCategory) -> Money:
        assert category in self.deductions, f"no deductions for {category}"
        return self.gross_income - self.deductions[category]

    def magi(self, category: TaxCategory) -> Money:
        assert category in self.magi_additions, (
            f"no MAGI additions for {category}"
        )
        return self.agi(category) + self.magi_additions[category]
