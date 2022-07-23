"""Contains a class representing a financial account."""

from typing import TypeVar


T = TypeVar("T")


class Account:
    """Represents a financial account."""

    def __init__(self, balance: T):
        self.balance = balance
