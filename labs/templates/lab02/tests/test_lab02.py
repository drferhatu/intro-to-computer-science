"""Tests for Lab 2. Run them with:  python3 check.py   (or: python3 -m pytest)"""
from conftest import run


# Part B ---------------------------------------------------------------------

def test_hello(hello):
    """hello.c prints "hello, world" """
    out = run(hello)
    assert out == "hello, world\n", f"expected 'hello, world\\n', got {out!r}"


# Part C ---------------------------------------------------------------------

def test_greet(greet):
    """greet.c greets the name it reads"""
    out = run(greet, "Firat\n")
    assert out.endswith("hello, Firat\n"), f"expected output to end with 'hello, Firat\\n', got {out!r}"


def test_greet_spaces(greet):
    """greet.c works for a name with spaces"""
    out = run(greet, "Ada Lovelace\n")
    assert out.endswith("hello, Ada Lovelace\n"), f"expected output to end with 'hello, Ada Lovelace\\n', got {out!r}"


# Part D ---------------------------------------------------------------------

def _last_line(out: str) -> str:
    return out.strip().splitlines()[-1].split(":")[-1].strip() if out.strip() else ""


def test_bits_73(bits):
    """bits.c prints 73 as 01001001"""
    assert _last_line(run(bits, "73\n")) == "01001001"


def test_bits_edges(bits):
    """bits.c prints 0 and 255 correctly"""
    assert _last_line(run(bits, "0\n")) == "00000000"
    assert _last_line(run(bits, "255\n")) == "11111111"
    assert _last_line(run(bits, "170\n")) == "10101010"
