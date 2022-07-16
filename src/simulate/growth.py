"""Utilities related to monetary growth."""

import math

from finances import Money

from .errors import SimulationParameterError


def _ensure_positive(number: float, description: str) -> None:
    if number <= 0.0:
        raise SimulationParameterError(
            f"{description} must be positive but is {number}"
        )


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
    _ensure_positive(growth_rate, "growth_rate")

    if growth_rate == 1.0:
        return accumulation_rate * time

    return accumulation_rate.grow_and_round(
        (growth_rate**time - 1) / math.log(growth_rate)
    )


def grow(principal: Money, growth_rate: float, time: int) -> Money:
    """
    Calculates a principal compounded over time.

    Arguments:
        principal - The starting amount of money.
        growth_rate - The rate at which to grow the money each time period. FOr
                      example, 1.0 means no change.
        time - The number of time periods to simulate.
    Return value: The compounded principal.
    """
    _ensure_positive(growth_rate, "growth_rate")

    return principal.grow_and_round(growth_rate**time)
