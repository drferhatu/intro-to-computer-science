"""Part D"""
from conftest import run, after_prompts


def pyramid(h):
    return "\n".join(" " * (h - i) + "#" * i for i in range(1, h + 1))


def test_mario_4(mario):
    """mario.c prints a right-aligned pyramid of height 4"""
    got = after_prompts(run(mario, "4\n"))
    assert got == pyramid(4), f"expected:\n{pyramid(4)}\ngot:\n{got}"


def test_mario_1_and_8(mario):
    """mario.c handles heights 1 and 8"""
    assert after_prompts(run(mario, "1\n")) == "#"
    assert after_prompts(run(mario, "8\n")) == pyramid(8)


def test_mario_reprompts(mario):
    """mario.c re-prompts on 0, 9 and -3, then accepts 3"""
    got = after_prompts(run(mario, "0\n9\n-3\n3\n"))
    assert got == pyramid(3), f"after rejecting 0, 9 and -3 the pyramid of height 3 should follow; got:\n{got}"
