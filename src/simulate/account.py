"""Contains a class representing a financial account."""

from __future__ import annotations

from typing import Generic

from finances.utilities import AddableT


class Account(Generic[AddableT]):
    """
    Represents a financial account.

    The account can contain any Addable type, such as Money or Value.

    Example: my_account = Account[Money](Money.of(314, 15))
    """

    def __init__(self, balance: AddableT):
        """
        Creates an Account with a starting balance.

        Arguments:
            balance - The initial balance of the account.
        """
        self._balance = balance

    def balance(self) -> AddableT:
        """Retrieves the current account balance."""
        return self._balance

    def __iadd__(self, other: AddableT) -> Account[AddableT]:
        """Adds other to this account's balance."""
        self._balance += other
        return self

    def __isub__(self, other: AddableT) -> Account[AddableT]:
        """Subtracts other from this account's balance."""
        self._balance -= other
        return self

    def __imul__(self, other: int) -> Account[AddableT]:
        """Multiplies this account's balance by an integer."""
        self._balance *= other
        return self

    def grow_and_round(self, ratio: float) -> Account[AddableT]:
        """Multiply's this account's balance by ratio, rounding."""
        self._balance = self._balance.grow_and_round(ratio)
        return self

    def transfer(
        self, amount: AddableT, to_account: Account[AddableT]
    ) -> Account[AddableT]:
        """
        Transfers an amount of this account's balance to another account.

        The amount and/or account balance can be negative.

        Arguments:
            amount - The amount to transfer.
            to_account - The acount to transfer amount to.
        Return value: This account.
        """
        self._balance -= amount
        to_account._balance += amount
        return self
