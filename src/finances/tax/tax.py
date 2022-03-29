from typing import Protocol

from ..earnings import Earnings
from ..money import Money

class IncomeTax(Protocol):
    def calculate(self, earnings: Earnings) -> Money:
        ...
