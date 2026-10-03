"""Part C"""
from conftest import run


def _last(out):
    return out.strip().splitlines()[-1].split(":")[-1].strip() if out.strip() else ""


def test_bits_73(bits):
    """bits.c prints 73 as 01001001"""
    assert _last(run(bits, "73\n")) == "01001001"


def test_bits_edges(bits):
    """bits.c prints 0, 255 and 170 correctly"""
    assert _last(run(bits, "0\n")) == "00000000"
    assert _last(run(bits, "255\n")) == "11111111"
    assert _last(run(bits, "170\n")) == "10101010"
