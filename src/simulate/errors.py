"""Simulation-related errors."""


class SimulationError(Exception):
    """An error raised during a simulation."""


class SimulationParameterError(SimulationError):
    """An error because of invalid simulation parameters."""


class SimulationInternalError(SimulationError):
    """An unexpected error that occurred while running a simulation."""
