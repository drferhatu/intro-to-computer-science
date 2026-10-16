"""Part A"""
from conftest import run

NUMS = [1, 5, 10, 20, 50, 100, 500]


def feed(nums, target):
    return f"{len(nums)}\n" + "\n".join(map(str, nums)) + f"\n{target}\n"


def lines(out):
    return [l[l.index(k):] for l in out.splitlines() for k in ("Linear:", "Binary:") if k in l]


def test_search_found(search):
    """search.c finds 50 at index 4: linear in 5 comparisons, binary in 3"""
    out, _ = run(search, feed(NUMS, 50))
    assert lines(out) == ["Linear: found at index 4 after 5 comparisons", "Binary: found at index 4 after 3 comparisons"], f"got {out!r}"


def test_search_first_and_last(search):
    """search.c: first element (linear 1 comparison) and last element (binary 3 comparisons)"""
    out, _ = run(search, feed(NUMS, 1))
    assert lines(out)[0] == "Linear: found at index 0 after 1 comparisons", f"got {out!r}"
    out, _ = run(search, feed(NUMS, 500))
    assert lines(out) == ["Linear: found at index 6 after 7 comparisons", "Binary: found at index 6 after 3 comparisons"], f"got {out!r}"


def test_search_missing(search):
    """search.c: a missing target is 'not found' after 7 (linear) and at most 3 (binary) comparisons"""
    out, _ = run(search, feed(NUMS, 7))
    got = lines(out)
    assert got[0] == "Linear: not found after 7 comparisons", f"got {out!r}"
    assert got[1].startswith("Binary: not found after ") and int(got[1].split()[4]) <= 3, f"got {out!r}"


def test_search_large(search):
    """search.c: 100 numbers, binary search needs at most 7 comparisons"""
    nums = list(range(2, 202, 2))
    out, _ = run(search, feed(nums, 150))
    got = lines(out)
    assert got[0] == "Linear: found at index 74 after 75 comparisons", f"got {out!r}"
    assert got[1].startswith("Binary: found at index 74 after ") and int(got[1].split()[6]) <= 7, f"got {out!r}"
