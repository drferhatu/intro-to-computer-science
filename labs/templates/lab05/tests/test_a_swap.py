"""Part A"""
from conftest import run


def test_swap_works(swap):
    """swap.c really swaps x and y"""
    out, _ = run(swap, "1\n2\n")[:2]
    assert out.endswith("x is 1, y is 2\nx is 2, y is 1\n"), f"got {out!r}"


def test_swap_uses_pointers():
    """swap.c declares void swap(int *a, int *b) and calls swap(&x, &y)"""
    from pathlib import Path
    src = (Path(__file__).resolve().parent.parent / "swap.c").read_text(encoding="utf-8")
    flat = " ".join(src.split())
    assert "swap(int *a, int *b)" in flat or "swap(int* a, int* b)" in flat, "the parameters must be pointers: int *a, int *b"
    assert "swap(&x, &y)" in flat, "main must pass the addresses: swap(&x, &y)"
