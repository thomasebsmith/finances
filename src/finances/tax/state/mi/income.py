"""Classes and utilities related to Michigan state income tax."""

from ....earnings import Earnings, EarningsTaxPolicy, TaxCategory
from ....money import Money
from ...flat import FlatTax


class MichiganIncomeTax:
    """Michigan state income tax."""

    def __init__(self, year: int):
        """
        Creates a MichiganIncomeTax.

        Arguments:
            year - The tax year.
        """
        assert year == 2021, f"No MI income tax data for {year}"
        self._underlying = FlatTax(
            rate=0.0425,
            policy=EarningsTaxPolicy(
                allow_deductions=True, category=TaxCategory.STATE
            ),
        )

    def calculate(self, earnings: Earnings) -> Money:
        """
        Calculates the amount of tax to be levied on earnings.

        Arguments:
            earnings - The earnings to tax.
        Return value: The Michigan state income tax on earnings.
        """
        return self._underlying.calculate(earnings)
