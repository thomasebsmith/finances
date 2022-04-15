"""Federal tax data (e.g. tax rates and thresholds)."""
from __future__ import annotations

from ...money import Money
from .status import FilingStatus

MEDICARE_TAX_DATA_YEARS = {2021, 2022}

MEDICARE_TAX_RATE = 0.0145

ADDITIONAL_MEDICARE_TAX_THRESHOLDS: dict[FilingStatus, Money] = {
    FilingStatus.MARRIED_FILING_JOINTLY: Money.of(250000),
    FilingStatus.MARRIED_FILING_SEPARATELY: Money.of(125000),
    **dict.fromkeys(
        [
            FilingStatus.SINGLE,
            FilingStatus.HEAD_OF_HOUSEHOLD,
            FilingStatus.SURVIVING_SPOUSE,
        ],
        Money.of(200000),
    ),
}

ADDITIONAL_MEDICARE_TAX_RATE = 0.009

SOCIAL_SECURITY_TAX_RATE = 0.062

WAGE_BASE_LIMIT_BY_YEAR: dict[int, Money] = {
    2021: Money.of(142800),
    2022: Money.of(147000),
}
