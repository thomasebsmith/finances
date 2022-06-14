"""Simulation-related errors."""


class SimulationError(Exception):
    """An error raised during a simulation."""


class SimulationParameterError(SimulationError):
    """An error because of invalid simulation parameters."""
