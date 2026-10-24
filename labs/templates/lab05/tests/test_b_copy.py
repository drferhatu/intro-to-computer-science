"""Part B"""
from conftest import run, need_valgrind


def test_copy_output(copy):
    """copy.c prints the original unchanged and the copy in uppercase"""
    out, code, _ = run(copy, "hello, world\n")
    assert code == 0
    assert out.endswith("s: hello, world\nt: HELLO, WORLD\n"), f"got {out!r}"


def test_copy_empty_and_mixed(copy):
    """copy.c handles an empty string and digits/punctuation"""
    out, _, _ = run(copy, "\n")
    assert out.endswith("s: \nt: \n"), f"got {out!r}"
    out, _, _ = run(copy, "Firat 2026!\n")
    assert out.endswith("s: Firat 2026!\nt: FIRAT 2026!\n"), f"got {out!r}"


def test_copy_valgrind_clean(copy):
    """copy.c has no memory errors and no leaks under valgrind"""
    need_valgrind()
    out, code, rep = run(copy, "memory\n", valgrind=True)
    assert code != 99 and "Invalid" not in rep, f"valgrind found errors:\n{rep[:800]}"
    assert "definitely lost" not in rep and "still reachable" not in rep.replace("still reachable: 0 bytes", ""), f"valgrind reports a leak:\n{rep[:800]}"
