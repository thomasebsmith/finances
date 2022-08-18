"""Contains a class for represention a financial simulation."""

from finances import Money

from .account import Account
from .errors import SimulationParameterError
from .growth import grow


class Simulation:
    """Represents a financial simulation."""

    def __init__(self, start: int, end: int):
        """
        Creates a simulation.

        Arguments:
            start - The year in which the simulation should start, inclusive.
            end - The year in which the simulation should end, exclusive.
        """
        if start > end:
            raise SimulationParameterError("end year must be after start")
        self.start = start
        self.end = end
        self.investments = Account(Money.of(1000))

    def run(self) -> None:
        """Runs the simulation."""
        print(f"Balance starting at {self.investments.balance()}")

        def grow_money(money: Money) -> Money:
            return grow(money, growth_rate=1.10, time=self.end - self.start)

        self.investments.apply(grow_money)

        print(f"Balance ending at {self.investments.balance()}")
