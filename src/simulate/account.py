"""Contains a class representing a financial account."""

from finances.utilities import AddableT


class Account:
    """
    Represents a financial account.

    The account can contain any Addable type, such as Money or Value.
    """

    def __init__(self, balance: AddableT):
        """
        Creates an Account.

        Arguments:
            balance - The initial balance of the account.
        """
        self._balance = balance

    def balance(self) -> AddableT:
        """Retrieves the account balance."""
        return self._balance

    def __iadd__(self, other: AddableT) -> None:
        """Adds other to this account's balance."""
        self._balance += other

    def __isub__(self, other: AddableT) -> None:
        """Subtracts other from this account's balance."""
        self._balance -= other

    def __imul__(self, other: int) -> None:
        """Multiplies this account's balance by an integer."""
        self._balance *= other
