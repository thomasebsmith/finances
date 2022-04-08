from ...earnings import Earnings, EarningsTaxPolicy
from ..composite import CompositeTax
from ..flat import FlatTax
from ...money import Money

WAGE_BASE_LIMIT_BY_YEAR = {
    2021: Money.of(142800, 0)
}

class SocialSecurityTax:
    def __init__(self, year: int):
        assert year in WAGE_BASE_LIMIT_BY_YEAR, (
            f"no social security tax data for {year}"
        )
        self._underlying = FlatTax(
            0.062,
            EarningsTaxPolicy(
                allow_deductions=False,
                ceiling=WAGE_BASE_LIMIT_BY_YEAR[year]
            )
        )

    def calculate(self, earnings: Earnings) -> Money:
        return self._underlying.calculate(earnings)

class MedicareTax:
    def __init__(self, year: int):
        assert year == 2021, f"no medicare tax data for {year}"
        self._underlying = FlatTax(
            0.0145,
            EarningsTaxPolicy(allow_deductions=False)
        )

    def calculate(self, earnings: Earnings) -> Money:
        return self._underlying.calculate(earnings)

class FICATax:
    def __init__(self, year: int):
        self._underlying = CompositeTax([
            SocialSecurityTax(year),
            MedicareTax(year),
        ])

    def calculate(self, earnings: Earnings) -> Money:
        return self._underlying.calculate(earnings)
