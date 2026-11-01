"""Part B"""
from conftest import run


def lines(out):
    return [l for l in out.replace("> ", "\n").split("\n") if l.strip()]


def test_queue_fifo(queue_exe):
    """queue.c: names come out in the order they went in; 'next' on an empty queue prints Empty"""
    out, code, _ = run(queue_exe, "add Mario\nadd Luigi\nnext\nnext\nnext\nquit\n")
    assert code == 0 and lines(out) == ["Mario", "Luigi", "Empty"], f"got {out!r}"


def test_queue_full_and_wraparound(queue_exe):
    """queue.c: a 5th 'add' prints Full; after removing, new names fit again (circular array)"""
    cmds = "add A\nadd B\nadd C\nadd D\nadd E\nnext\nnext\nadd F\nadd G\nnext\nnext\nnext\nnext\nnext\nquit\n"
    out, _, _ = run(queue_exe, cmds)
    assert lines(out) == ["Full", "A", "B", "C", "D", "F", "G", "Empty"], f"got {out!r}"
