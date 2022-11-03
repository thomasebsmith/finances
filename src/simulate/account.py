"""Contains a class representing a financial account."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Generic, TypeVar

from finances.utilities import Growable


GrowableT = TypeVar("GrowableT", bound=Growable)


@dataclass(frozen=False, order=True)
class Account(Generic[GrowableT]):
    """
    Represents a financial account.

    The account can contain any Addable and Comparable type, such as Money or
    Value.

    Example: my_account = Account[Money](Money.of(314, 15))
    """

    _balance: GrowableT

    def balance(self) -> GrowableT:
        """Retrieves the current account balance."""
        return self._balance

    def __iadd__(self, other: GrowableT) -> Account[GrowableT]:
        """Adds other to this account's balance."""
        self._balance += other
        return self

    def __isub__(self, other: GrowableT) -> Account[GrowableT]:
        """Subtracts other from this account's balance."""
        self._balance -= other
        return self

    def __imul__(self, other: int) -> Account[GrowableT]:
        """Multiplies this account's balance by an integer."""
        self._balance *= other
        return self

    def grow_and_round(self, ratio: float) -> Account[GrowableT]:
        """Multiply's this account's balance by ratio, rounding."""
        self._balance = self._balance.grow_and_round(ratio)
        return self

    def transfer(
        self,
        amount: GrowableT,
        to_account: Account[GrowableT],
    ) -> Account[GrowableT]:
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

    def apply(
        self,
        balance_modifier: Callable[[GrowableT], GrowableT],
    ) -> Account[GrowableT]:
        """
        Applies balance_modifier to this account's balance.

        Arguments:
            balance_modifier - A function to call on this account's balance.
                The account's new balance will be set to its return value.
        Return value: This account.
        """
        self._balance = balance_modifier(self._balance)
        return self
