"""Classes and utilities related to Michigan state income tax."""

from ....earnings import EarningsTaxPolicy, TaxCategory
from ...flat import FlatTax

MICHIGAN_TAX_DATA_YEARS = {2021, 2022}


class MichiganIncomeTax(FlatTax):
    """Michigan state income tax."""

    def __init__(self, year: int):
        """
        Creates a MichiganIncomeTax.

        Arguments:
            year - The tax year.
        """
        assert (
            year in MICHIGAN_TAX_DATA_YEARS
        ), f"No MI income tax data for {year}"
        super().__init__(
            rate=0.0425,
            policy=EarningsTaxPolicy(
                allow_deductions=True, category=TaxCategory.STATE
            ),
        )
