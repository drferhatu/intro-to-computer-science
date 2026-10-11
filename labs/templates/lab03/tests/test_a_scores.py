"""Part A"""
from conftest import run


def lines(out):
    # keep only lines that start with Min/Max/Average (prompts are on the same line as the first answer)
    return [l[l.index(k):] for l in out.splitlines() for k in ("Min:", "Max:", "Average:") if k in l]


def test_scores_three(scores):
    """scores.c: 72, 73, 33 → Min 33, Max 73, Average 59.33"""
    out, _ = run(scores, "3\n72\n73\n33\n")
    assert lines(out) == ["Min: 33", "Max: 73", "Average: 59.33"], f"got {out!r}"


def test_scores_one_and_ten(scores):
    """scores.c works for 1 score and for 10 scores"""
    out, _ = run(scores, "1\n50\n")
    assert lines(out) == ["Min: 50", "Max: 50", "Average: 50.00"], f"got {out!r}"
    out, _ = run(scores, "10\n" + "\n".join(map(str, range(1, 11))) + "\n")
    assert lines(out) == ["Min: 1", "Max: 10", "Average: 5.50"], f"got {out!r}"


def test_scores_reprompts(scores):
    """scores.c re-prompts on 0 and 11 before accepting 2"""
    out, _ = run(scores, "0\n11\n2\n90\n80\n")
    assert lines(out) == ["Min: 80", "Max: 90", "Average: 85.00"], f"got {out!r}"
