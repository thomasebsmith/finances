"""Tests of src/simulate/account.py."""

from finances import Money, Value
from simulate.account import Account


def test_init_and_balance() -> None:
    """Tests the behavior of Account.__init__ and Account.balance."""
    assert Account[Money](Money.of(314, 15)).balance() == Money.of(314, 15)
    assert Account[Money](Money.of(-128)).balance() == Money.of(-128)
    assert Account[Money](Money.of(0, 20)).balance() == Money.of(0, 20)
    assert Account[Money](Money.of(-56, 99)).balance() == Money.of(-56, 99)


def test_add() -> None:
    """Tests the behavior of Account.__iadd__."""
    acct = Account[Money](Money.of(8220, 9))
    acct += Money.of(-8219, 8)
    assert acct.balance() == Money.of(1, 1)
    acct += Money.of(3, 14)
    assert acct.balance() == Money.of(4, 15)

    acct2 = Account[Value](
        Value.of_inflated_money(Money.of(123, 45), inflation_since_2000=0.0)
    )
    acct2 += Value.of_inflated_money(
        Money.of(-100), inflation_since_2000=-0.091
    )
    acct2 += Value.of_inflated_money(Money.of(15, 15), inflation_since_2000=0.5)
    assert acct2.balance() == Value.of_inflated_money(
        Money.of(23, 54), inflation_since_2000=0.0
    )
