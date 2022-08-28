"""Contains a class representing a financial account."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Generic, TypeVar

from finances.utilities import AddableComparable


AddableComparableT = TypeVar("AddableComparableT", bound=AddableComparable)


@dataclass(frozen=False, order=True)
class Account(Generic[AddableComparableT]):
    """
    Represents a financial account.

    The account can contain any Addable and Comparable type, such as Money or
    Value.

    Example: my_account = Account[Money](Money.of(314, 15))
    """

    _balance: AddableComparableT

    def balance(self) -> AddableComparableT:
        """Retrieves the current account balance."""
        return self._balance

    def __iadd__(
        self, other: AddableComparableT
    ) -> Account[AddableComparableT]:
        """Adds other to this account's balance."""
        self._balance += other
        return self

    def __isub__(
        self, other: AddableComparableT
    ) -> Account[AddableComparableT]:
        """Subtracts other from this account's balance."""
        self._balance -= other
        return self

    def __imul__(self, other: int) -> Account[AddableComparableT]:
        """Multiplies this account's balance by an integer."""
        self._balance *= other
        return self

    def grow_and_round(self, ratio: float) -> Account[AddableComparableT]:
        """Multiply's this account's balance by ratio, rounding."""
        self._balance = self._balance.grow_and_round(ratio)
        return self

    def transfer(
        self,
        amount: AddableComparableT,
        to_account: Account[AddableComparableT],
    ) -> Account[AddableComparableT]:
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
        balance_modifier: Callable[[AddableComparableT], AddableComparableT],
    ) -> Account[AddableComparableT]:
        """
        Applies balance_modifier to this account's balance.

        Arguments:
            balance_modifier - A function to call on this account's balance.
                The account's new balance will be set to its return value.
        Return value: This account.
        """
        self._balance = balance_modifier(self._balance)
        return self
