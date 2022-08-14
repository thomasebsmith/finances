"""Contains a class for represention a financial simulation."""

from finances import Money

from .account import Account


class Simulation:
    """Represents a financial simulation."""

    def __init__(self, start: int, end: int):
        """
        Creates a simulation.

        Arguments:
            start - The year in which the simulation should start, inclusive.
            end - The year in which the simulation should end, exclusive.
        """
        self.start = start
        self.end = end
        self.investments = Account(Money.of(1000))

    def run(self) -> None:
        """Runs the simulation."""
        print(f"Balance starting at {self.investments.balance()}")

        growth_rate = 1.10
        for _ in range(self.start, self.end):
            self.investments.grow_and_round(growth_rate)

        print(f"Balance ending at {self.investments.balance()}")
