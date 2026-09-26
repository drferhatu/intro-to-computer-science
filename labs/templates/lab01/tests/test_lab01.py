"""Tests for Lab 1. Run them with:  python3 check.py   (or: python3 -m pytest)"""
import re
from pathlib import Path

from conftest import ROOT, run


# Part A ---------------------------------------------------------------------

def test_readme_scratch_link():
    """README links a Scratch project"""
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    m = re.search(r"https://scratch\.mit\.edu/projects/\d+/?", text)
    assert m, "no scratch.mit.edu/projects/ link found in README.md (Share → Copy Link in Scratch, then paste it after 'Scratch:')"


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
