"""Part F"""
from conftest import run, after_prompts


def coins(c):
    n = 0
    for v in (25, 10, 5, 1):
        n += c // v
        c %= v
    return n


def test_cash_41(cash):
    """cash.c: 41 cents is 4 coins"""
    assert after_prompts(run(cash, "41\n")) == "4"


def test_cash_values(cash):
    """cash.c: 0, 1, 25, 99 and 160 cents"""
    for c in (0, 1, 25, 99, 160):
        got = after_prompts(run(cash, f"{c}\n"))
        assert got == str(coins(c)), f"{c} cents should be {coins(c)} coins, got {got!r}"


def test_cash_reprompts(cash):
    """cash.c re-prompts on a negative amount, then accepts 30 (a quarter and a nickel)"""
    assert after_prompts(run(cash, "-1\n30\n")) == "2"
