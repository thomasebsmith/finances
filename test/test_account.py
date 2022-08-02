"""Tests of src/simulate/account.py."""

from finances import Money
from simulate.account import Account


def test_init_and_balance() -> None:
    """Tests the behavior of Account.__init__ and Account.balance."""
    assert Account[Money](Money.of(314, 15)).balance() == Money.of(314, 15)
    assert Account[Money](Money.of(-128)).balance() == Money.of(-128)
    assert Account[Money](Money.of(0, 20)).balance() == Money.of(0, 20)
    assert Account[Money](Money.of(-56, 99)).balance() == Money.of(-56, 99)
