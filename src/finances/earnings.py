"""Classes related to a tax-filer's earnings for the year."""

from __future__ import annotations

from dataclasses import dataclass
from enum import auto, Enum
from typing import Optional

from .money import Money


class TaxCategory(Enum):
    """A classification of a tax and the level at which it is applied."""

    FEDERAL = auto()
    STATE = auto()
    LOCAL = auto()


@dataclass(frozen=True)
class EarningsTaxPolicy:
    """A specification of to which earnings a tax applies."""

    allow_deductions: bool
    category: TaxCategory
    floor: Optional[Money] = None
    ceiling: Optional[Money] = None

    def __post_init__(self) -> None:
        if self.floor is not None and self.ceiling is not None:
            assert self.floor <= self.ceiling, "floor must not exceed ceiling"


@dataclass(frozen=True)
class Earnings:
    """Information about an individual's taxable earnings for the year."""

    gross_income: Money
    deductions: dict[TaxCategory, Money]
    magi_additions: dict[TaxCategory, Money]

    def taxable_income(self, policy: EarningsTaxPolicy) -> Money:
        """
        Calculates how much of these earnings are taxable under policy.

        Arguments:
            policy - A tax policy to use to determine which earnings are taxable
        Return value: The amount of taxable income
        """
        income = (
            self.agi(policy.category)
            if policy.allow_deductions
            else self.gross_income
        )

        if policy.floor is not None:
            income = max(policy.floor, income)
        if policy.ceiling is not None:
            income = min(policy.ceiling, income)

        return income

    def agi(self, category: TaxCategory) -> Money:
        """
        Calculates the adjusted gross income of these earnings for category.

        Arguments:
            category - The category to use to determine deductions, etc.
        Return value: The AGI
        """
        assert category in self.deductions, f"no deductions for {category}"
        return self.gross_income - self.deductions[category]

    def magi(self, category: TaxCategory) -> Money:
        """
        Calculates the modified adjusted gross income for category.

        Arguments:
            category - The category to use to determine deductions, etc.
        Return value: The MAGI
        """
        assert (
            category in self.magi_additions
        ), f"no MAGI additions for {category}"
        return self.agi(category) + self.magi_additions[category]
