"""Part E"""
from conftest import run, after_prompts


def test_calculator_7_2(calculator):
    """calculator.c prints 9 5 14 3.50 1 for x=7, y=2"""
    got = after_prompts(run(calculator, "7\n2\n")).splitlines()
    assert got == ["9", "5", "14", "3.50", "1"], f"got {got}"


def test_calculator_negative_and_truncation(calculator):
    """calculator.c: x=1, y=3 gives 4 -2 3 0.33 1 (real division, not truncated)"""
    got = after_prompts(run(calculator, "1\n3\n")).splitlines()
    assert got == ["4", "-2", "3", "0.33", "1"], f"got {got}"


def test_calculator_div_zero(calculator):
    """calculator.c prints undefined twice when y is 0 instead of crashing"""
    got = after_prompts(run(calculator, "5\n0\n")).splitlines()
    assert got == ["5", "5", "0", "undefined", "undefined"], f"got {got}"
