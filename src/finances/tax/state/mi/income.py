"""Classes and utilities related to Michigan state income tax."""

from ....earnings import EarningsTaxPolicy, EarningsType, TaxCategory
from ...flat import FlatTax
from .data import MICHIGAN_INCOME_TAX_RATE_BY_YEAR


class MichiganIncomeTax(FlatTax):
    """Michigan state income tax."""

    def __init__(self, year: int):
        """
        Creates a MichiganIncomeTax.

        Arguments:
            year - The tax year.
        """
        assert (
            year in MICHIGAN_INCOME_TAX_RATE_BY_YEAR
        ), f"No MI income tax data for {year}"
        super().__init__(
            rate=MICHIGAN_INCOME_TAX_RATE_BY_YEAR[year],
            policy=EarningsTaxPolicy(
                earnings_type=EarningsType.AGI_WITH_DEDUCTIONS,
                category=TaxCategory.STATE,
            ),
        )
