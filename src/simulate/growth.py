"""Utilities related to monetary growth."""

import math

from finances import Money

from .errors import SimulationParameterError


def accumulate_and_grow(
    accumulation_rate: Money, growth_rate: float, time: int
) -> Money:
    """
    Calculates money accumulated and compounded over time.

    Specifically, calculates the amount of money obtained by continuously adding
    accumulation_rate over each time period with compounded growth at
    growth_rate for time time periods.

    Arguments:
        accumulation_rate - The amount of money to add each time period.
        growth_rate - The rate at which to grow all money each time period. For
                      example, 1.0 means no change.
        time - The number of time periods to simulate.
    Return value: The amount of money accumulated.
    """
    if growth_rate <= 0.0:
        raise SimulationParameterError(
            f"growth_rate must be positive but is {growth_rate}"
        )

    if growth_rate == 1.0:
        return accumulation_rate * time

    return accumulation_rate.grow_and_round(
        (growth_rate**time - 1) / math.log(growth_rate)
    )
