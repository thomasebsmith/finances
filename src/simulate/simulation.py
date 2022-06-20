"""Contains a class for represention a financial simulation."""


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

    def run(self):
        """Runs the simulation."""
        print("Hello from simulate!")
        print(f"Starting in {self.start}")
        print(f"Ending before {self.end}")
