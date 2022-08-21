"""Contains a class for represention a financial simulation."""

from typing import Protocol

from finances import Money

from .account import Account
from .errors import SimulationParameterError
from .growth import grow


class Simulation(Protocol):
    """Represents a financial simulation."""

    def run(self, iterations: int) -> None:
        """Runs this simulation a number of times."""


class BasicSimulation(Simulation):
    """Represents a basic financial simulation."""

    def __init__(self, start: int, end: int, starting_balance: Money):
        """
        Creates a basic simulation.

        Arguments:
            start - The year in which the simulation should start, inclusive.
            end - The year in which the simulation should end, exclusive.
            starting_balance - The balance the simulation should start with.
        """
        if start > end:
            raise SimulationParameterError("end year must be after start")
        self.start = start
        self.end = end
        self.investments = Account(starting_balance)

    def run(self, iterations: int) -> None:
        """Runs the simulation."""
        print(f"Balance starting at {self.investments.balance()}")

        def grow_money(money: Money) -> Money:
            return grow(money, growth_rate=1.10, time=self.end - self.start)

        self.investments.apply(grow_money)

        print(f"Balance ending at {self.investments.balance()}")
