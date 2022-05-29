"""Contains a class for represention a financial simulation."""


class Simulation:
    """Represents a financial simulation."""

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def run(self):
        """Runs the simulation."""
        print("Hello from simulate!")
        print(f"Starting in {self.start}")
        print(f"Ending in {self.end}")
