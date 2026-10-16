"""Part B"""
import random
from conftest import run, after_prompts


def feed(nums):
    return f"{len(nums)}\n" + "\n".join(map(str, nums)) + "\n"


def test_sort_usage(sort):
    """sort.c prints the usage line and returns 1 for no, two, or an unknown argument"""
    for args in [(), ("bubble", "x"), ("quick",)]:
        out, code = run(sort, "", args)
        assert "Usage: ./sort selection|bubble" in out and code == 1, f"args {args}: got {out!r}, exit {code}"


def test_selection_small(sort):
    """./sort selection sorts 6 3 8 1 2 → 1 2 3 6 8"""
    out, code = run(sort, feed([6, 3, 8, 1, 2]), ("selection",))
    assert code == 0 and after_prompts(out) == "1 2 3 6 8", f"got {out!r}"


def test_bubble_small(sort):
    """./sort bubble sorts 6 3 8 1 2 → 1 2 3 6 8"""
    out, code = run(sort, feed([6, 3, 8, 1, 2]), ("bubble",))
    assert code == 0 and after_prompts(out) == "1 2 3 6 8", f"got {out!r}"


def test_both_random_and_edge_cases(sort):
    """both sorts handle duplicates, negatives, one element and 100 random numbers"""
    random.seed(4)
    cases = [[5, 5, 5], [-3, 0, -10, 7], [42], [3, 2, 1], [random.randint(-50, 50) for _ in range(100)]]
    for alg in ("selection", "bubble"):
        for nums in cases:
            out, _ = run(sort, feed(nums), (alg,))
            assert after_prompts(out) == " ".join(map(str, sorted(nums))), f"{alg} on {nums[:6]}…: got {after_prompts(out)!r}"
