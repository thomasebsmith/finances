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


class EarningsType(Enum):
    """A type of earnings with certain deductions or adjustments applied."""

    GROSS_INCOME = auto()
    MAGI = auto()
    AGI = auto()
    AGI_WITH_DEDUCTIONS = auto()


@dataclass(frozen=True)
class EarningsTaxPolicy:
    """A specification of to which earnings a tax applies."""

    earnings_type: EarningsType
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
    adjustments: dict[TaxCategory, Money]
    deductions: dict[TaxCategory, Money]
    magi_additions: dict[TaxCategory, Money]

    def taxable_income(self, policy: EarningsTaxPolicy) -> Money:
        """
        Calculates how much of these earnings are taxable under policy.

        Arguments:
            policy - A tax policy to use to determine which earnings are taxable
        Return value: The amount of taxable income
        """
        income = self.of_type(policy.category, policy.earnings_type)

        if policy.floor is not None:
            income = max(policy.floor, income)
        if policy.ceiling is not None:
            income = min(policy.ceiling, income)

        return income

    def of_type(
        self,
        category: TaxCategory,
        earnings_type: EarningsType,
    ) -> Money:
        """
        Calculates the amount of earnings of the specified type.

        Arguments:
            category - The category to use to determine deductions, etc.
            earnings_type - The type of earnings to retrieve
        Return value: The earnings of the specified type
        """
        if earnings_type is EarningsType.GROSS_INCOME:
            return self.gross_income
        elif earnings_type is EarningsType.MAGI:
            return self.magi(category)
        elif earnings_type is EarningsType.AGI:
            return self.agi(category)
        else:
            return self.agi_with_deductions(category)

    def agi_with_deductions(self, category: TaxCategory) -> Money:
        """
        Calculates the AGI minus any deductions.

        Arguments:
            category - The category to use to determine deductions, etc.
        Return value: The AGI minus deductions
        """
        assert category in self.deductions, f"no deductions for {category}"
        return self.agi(category) - self.deductions[category]

    def agi(self, category: TaxCategory) -> Money:
        """
        Calculates the adjusted gross income of these earnings for category.

        Arguments:
            category - The category to use to determine adjustments, etc.
        Return value: The AGI
        """
        assert category in self.adjustments, f"no adjustments for {category}"
        return self.gross_income - self.adjustments[category]

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
