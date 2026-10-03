"""Part B"""
from conftest import run


def test_greet(greet):
    """greet.c greets the name it reads"""
    out = run(greet, "Firat\n")
    assert out.endswith("hello, Firat\n"), f"expected output to end with 'hello, Firat\\n', got {out!r}"


def test_greet_spaces(greet):
    """greet.c works for a name with spaces"""
    out = run(greet, "Ada Lovelace\n")
    assert out.endswith("hello, Ada Lovelace\n"), f"expected output to end with 'hello, Ada Lovelace\\n', got {out!r}"
