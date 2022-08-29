"""Contains a class that represents a probability."""

from fractions import Fraction

from .errors import SimulationInternalError


class Probability:
    """Represents the probability of an event."""

    def __init__(self, value: Fraction) -> None:
        """
        Initializes this probability, where 0 is 0% and 1 is 100%.

        value must be between 0 and 1.
        """
        if value < 0 or value > 1:
            raise SimulationInternalError(f"Invalid probability {value}")
        self._value = value

    def value(self) -> Fraction:
        """Returns this probability's value (in the range 0-1)."""
        return self._value
