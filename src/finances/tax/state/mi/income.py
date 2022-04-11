"""Classes and utilities related to Michigan state income tax."""

from ....earnings import EarningsTaxPolicy, TaxCategory
from ...flat import FlatTax


class MichiganIncomeTax(FlatTax):
    """Michigan state income tax."""

    def __init__(self, year: int):
        """
        Creates a MichiganIncomeTax.

        Arguments:
            year - The tax year.
        """
        assert year == 2021, f"No MI income tax data for {year}"
        super().__init__(
            rate=0.0425,
            policy=EarningsTaxPolicy(
                allow_deductions=True, category=TaxCategory.STATE
            ),
        )
