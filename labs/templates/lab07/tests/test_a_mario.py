"""Part A"""
from conftest import run, after_prompts, pyramid


def test_mario_4():
    """mario.py prints a right-aligned pyramid of height 4"""
    out, _ = run("mario.py", "4\n")
    got = after_prompts(out)
    assert got == pyramid(4), f"expected:\n{pyramid(4)}\ngot:\n{got}"


def test_mario_1_and_8():
    """mario.py handles heights 1 and 8"""
    assert after_prompts(run("mario.py", "1\n")[0]) == "#"
    assert after_prompts(run("mario.py", "8\n")[0]) == pyramid(8)


def test_mario_reprompts():
    """mario.py re-prompts on 'cat', 0, 9 and -3, then accepts 3"""
    out, _ = run("mario.py", "cat\n0\n9\n-3\n3\n")
    assert out.count("Height: ") == 5, f"expected 5 prompts (4 rejected inputs), got {out.count('Height: ')}"
    assert after_prompts(out) == pyramid(3), f"after rejecting cat, 0, 9 and -3 the pyramid of height 3 should follow; got:\n{after_prompts(out)}"
