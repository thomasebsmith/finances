"""Classes and utilities related to federal filing statuses."""

from enum import auto, Enum


class FilingStatus(Enum):
    """A federal filing status."""

    SINGLE = auto()
    MARRIED_FILING_JOINTLY = auto()
    MARRIED_FILING_SEPARATELY = auto()
    HEAD_OF_HOUSEHOLD = auto()
    SURVIVING_SPOUSE = auto()
