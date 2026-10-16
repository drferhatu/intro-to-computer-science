"""Part C"""
from conftest import run


def pyramid(h):
    return "\n".join("#" * i for i in range(1, h + 1))


def parts(out):
    """(pyramid text, factorial line)"""
    text = out.replace("Height: ", "").replace("n: ", "")
    lines = [l for l in text.splitlines() if l.strip()]
    fact = [l for l in lines if "!" in l]
    pyr = [l for l in lines if set(l) == {"#"}]
    return "\n".join(pyr), (fact[0] if fact else "")


def test_recursion_pyramid(recursion):
    """recursion.c draws a left-aligned pyramid of height 3 and of height 1"""
    out, _ = run(recursion, "3\n5\n")
    assert parts(out)[0] == pyramid(3), f"got {out!r}"
    out, _ = run(recursion, "1\n0\n")
    assert parts(out)[0] == "#", f"got {out!r}"


def test_recursion_factorial(recursion):
    """recursion.c: 5! = 120, 0! = 1, 20! = 2432902008176640000"""
    for n, f in [(5, 120), (0, 1), (20, 2432902008176640000), (10, 3628800)]:
        out, _ = run(recursion, f"1\n{n}\n")
        assert parts(out)[1] == f"{n}! = {f}", f"n={n}: got {out!r}"


def test_recursion_reprompts(recursion):
    """recursion.c re-prompts on a height of 21 and -1, and on n = 25"""
    out, _ = run(recursion, "21\n-1\n2\n25\n3\n")
    assert parts(out) == (pyramid(2), "3! = 6"), f"got {out!r}"


def test_recursion_is_recursive():
    """factorial has no loop and draw calls itself (recursion is the point)"""
    from pathlib import Path
    src = (Path(__file__).resolve().parent.parent / "recursion.c").read_text(encoding="utf-8")
    body = src.split("long factorial(int n)")[-1]
    assert "factorial(" in body.split("{", 1)[1], "factorial must call itself"
    assert "for (" not in body and "while (" not in body, "no loops inside factorial: use recursion"
    draw_body = src.split("void draw(int n)")[-1].split("long factorial")[0]
    assert "draw(" in draw_body.split("{", 1)[1], "draw must call itself"
