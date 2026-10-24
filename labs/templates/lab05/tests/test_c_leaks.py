"""Part C"""
from conftest import run, need_valgrind


def test_leaks_valgrind_clean(leaks):
    """leaks.c prints the right sum (n = 4 → 10, n = 100 → 5050) with 0 valgrind errors and no leaks"""
    need_valgrind()
    out, code, rep = run(leaks, "4\n", valgrind=True)
    assert out.endswith("sum = 10\n"), f"got {out!r}"
    out, code, rep = run(leaks, "100\n", valgrind=True)
    assert out.endswith("sum = 5050\n"), f"got {out!r}"
    assert code != 99 and "Invalid write" not in rep and "Invalid read" not in rep, f"valgrind found memory errors:\n{rep[:800]}"
    assert "definitely lost" not in rep, f"valgrind reports a leak (missing free?):\n{rep[:800]}"


def test_leaks_fixed_in_source():
    """leaks.c allocates n * sizeof(int), loops with i < n, and frees"""
    from pathlib import Path
    src = (Path(__file__).resolve().parent.parent / "leaks.c").read_text(encoding="utf-8")
    flat = " ".join(src.split())
    assert "malloc(n)" not in flat, "malloc(n) allocates n BYTES, not n ints"
    assert "i <= n" not in flat, "the fill loop runs one step too far"
    assert "free(numbers)" in flat, "the heap memory is never freed"
