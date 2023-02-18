"""Contains classes and utilities related to federal income tax."""

from __future__ import annotations

from ...earnings import EarningsTaxPolicy, EarningsType, TaxCategory
from ...money import Money
from ..bracket import Bracket, BracketTax
from .status import FilingStatus


def _joint_brackets(
    brackets: list[Bracket],
) -> dict[FilingStatus, list[Bracket]]:
    return dict.fromkeys(
        [FilingStatus.MARRIED_FILING_JOINTLY, FilingStatus.SURVIVING_SPOUSE],
        brackets,
    )


BRACKETS_BY_YEAR: dict[int, dict[FilingStatus, list[Bracket]]] = {
    2021: {
        **_joint_brackets(
            [
                Bracket(0.37, Money.of(628300)),
                Bracket(0.35, Money.of(418850)),
                Bracket(0.32, Money.of(329850)),
                Bracket(0.24, Money.of(172750)),
                Bracket(0.22, Money.of(81050)),
                Bracket(0.12, Money.of(19900)),
                Bracket(0.10, Money.of(0)),
            ]
        ),
        FilingStatus.HEAD_OF_HOUSEHOLD: [
            Bracket(0.37, Money.of(523600)),
            Bracket(0.35, Money.of(209400)),
            Bracket(0.32, Money.of(164900)),
            Bracket(0.24, Money.of(86350)),
            Bracket(0.22, Money.of(54200)),
            Bracket(0.12, Money.of(14200)),
            Bracket(0.10, Money.of(0)),
        ],
        FilingStatus.SINGLE: [
            Bracket(0.37, Money.of(523600)),
            Bracket(0.35, Money.of(209425)),
            Bracket(0.32, Money.of(164925)),
            Bracket(0.24, Money.of(86375)),
            Bracket(0.22, Money.of(40525)),
            Bracket(0.12, Money.of(9950)),
            Bracket(0.10, Money.of(0)),
        ],
        FilingStatus.MARRIED_FILING_SEPARATELY: [
            Bracket(0.37, Money.of(314150)),
            Bracket(0.35, Money.of(209425)),
            Bracket(0.32, Money.of(164925)),
            Bracket(0.24, Money.of(86375)),
            Bracket(0.22, Money.of(40525)),
            Bracket(0.12, Money.of(9950)),
            Bracket(0.10, Money.of(0)),
        ],
    },
    2022: {
        **_joint_brackets(
            [
                Bracket(0.37, Money.of(647850)),
                Bracket(0.35, Money.of(431900)),
                Bracket(0.32, Money.of(340100)),
                Bracket(0.24, Money.of(178150)),
                Bracket(0.22, Money.of(83550)),
                Bracket(0.12, Money.of(20550)),
                Bracket(0.10, Money.of(0)),
            ]
        ),
        FilingStatus.HEAD_OF_HOUSEHOLD: [
            Bracket(0.37, Money.of(539900)),
            Bracket(0.35, Money.of(215950)),
            Bracket(0.32, Money.of(170050)),
            Bracket(0.24, Money.of(89050)),
            Bracket(0.22, Money.of(55900)),
            Bracket(0.12, Money.of(14650)),
            Bracket(0.10, Money.of(0)),
        ],
        FilingStatus.SINGLE: [
            Bracket(0.37, Money.of(539900)),
            Bracket(0.35, Money.of(215950)),
            Bracket(0.32, Money.of(170050)),
            Bracket(0.24, Money.of(89075)),
            Bracket(0.22, Money.of(41775)),
            Bracket(0.12, Money.of(10275)),
            Bracket(0.10, Money.of(0)),
        ],
        FilingStatus.MARRIED_FILING_SEPARATELY: [
            Bracket(0.37, Money.of(323925)),
            Bracket(0.35, Money.of(215950)),
            Bracket(0.32, Money.of(170050)),
            Bracket(0.24, Money.of(89075)),
            Bracket(0.22, Money.of(41775)),
            Bracket(0.12, Money.of(10275)),
            Bracket(0.10, Money.of(0)),
        ],
    },
}


class FederalIncomeTax(BracketTax):
    """The United States federal income tax."""

    def __init__(self, year: int, filing_status: FilingStatus):
        """
        Creates a FederalIncomeTax.

        Arguments:
            year - The tax year.
            filing_status - The tax filer's filing status.
        """
        assert year in BRACKETS_BY_YEAR, f"No tax data for year {year}"
        assert (
            filing_status in BRACKETS_BY_YEAR[year]
        ), f"Invalid filing status {filing_status} for year {year}"

        super().__init__(
            BRACKETS_BY_YEAR[year][filing_status],
            policy=EarningsTaxPolicy(
                earnings_type=EarningsType.AGI_WITH_DEDUCTIONS,
                category=TaxCategory.FEDERAL,
            ),
        )
