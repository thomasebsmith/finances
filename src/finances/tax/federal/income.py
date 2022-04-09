from __future__ import annotations

from ...earnings import Earnings, EarningsTaxPolicy, TaxCategory
from ...money import Money
from ..bracket import Bracket, BracketTax
from .status import FilingStatus

def _joint_brackets(
    brackets: list[Bracket]
) -> dict[FilingStatus, list[Bracket]]:
    return dict.fromkeys([
        FilingStatus.MARRIED_FILING_JOINTLY,
        FilingStatus.SURVIVING_SPOUSE
    ], brackets)

BRACKETS_BY_YEAR: dict[int, dict[FilingStatus, list[Bracket]]] = {
    2021: {
        **_joint_brackets([
            Bracket(0.37, Money.of(628300)),
            Bracket(0.35, Money.of(418850)),
            Bracket(0.32, Money.of(329850)),
            Bracket(0.24, Money.of(172750)),
            Bracket(0.22,  Money.of(81050)),
            Bracket(0.12,  Money.of(19900)),
            Bracket(0.10,      Money.of(0)),
        ]),
        FilingStatus.HEAD_OF_HOUSEHOLD: [
            Bracket(0.37, Money.of(523600)),
            Bracket(0.35, Money.of(209400)),
            Bracket(0.32, Money.of(164900)),
            Bracket(0.24,  Money.of(86350)),
            Bracket(0.22,  Money.of(54200)),
            Bracket(0.12,  Money.of(14200)),
            Bracket(0.10,      Money.of(0)),
        ],
        FilingStatus.SINGLE: [
            Bracket(0.37, Money.of(523600)),
            Bracket(0.35, Money.of(209425)),
            Bracket(0.32, Money.of(164925)),
            Bracket(0.24,  Money.of(86375)),
            Bracket(0.22,  Money.of(40525)),
            Bracket(0.12,   Money.of(9950)),
            Bracket(0.10,      Money.of(0)),
        ],
        FilingStatus.MARRIED_FILING_SEPARATELY: [
            Bracket(0.37, Money.of(314150)),
            Bracket(0.35, Money.of(209425)),
            Bracket(0.32, Money.of(164925)),
            Bracket(0.24,  Money.of(86375)),
            Bracket(0.22,  Money.of(40525)),
            Bracket(0.12,   Money.of(9950)),
            Bracket(0.10,      Money.of(0)),
        ],
    }
}

class FederalIncomeTax:
    def __init__(self, year: int, filing_status: FilingStatus):
        assert year in BRACKETS_BY_YEAR, f"No tax data for year {year}"
        assert filing_status in BRACKETS_BY_YEAR[year], (
            f"Invalid filing status {filing_status} for year {year}"
        )

        self._underlying = BracketTax(
            BRACKETS_BY_YEAR[year][filing_status],
            policy=EarningsTaxPolicy(
                allow_deductions=True,
                category=TaxCategory.FEDERAL
            )
        )

    def calculate(self, earnings: Earnings) -> Money:
        return self._underlying.calculate(earnings)
