"""Contains a class representing a financial account."""

from finances.utilities import AddableT


class Account:
    """Represents a financial account."""

    def __init__(self, balance: AddableT):
        self.balance = balance
