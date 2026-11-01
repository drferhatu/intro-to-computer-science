"""Part A"""
from conftest import run, need_valgrind


def body(out):
    return out.replace("Number (0 to stop): ", "").replace("Target: ", "")


def test_list_order_and_found(list_exe):
    """list.c: 1 2 3 inserted at the head prints 'List: 3 2 1' and finds 2"""
    out, code, _ = run(list_exe, "1\n2\n3\n0\n2\n")
    assert code == 0 and "List: 3 2 1\n" in body(out) and body(out).rstrip().endswith("Found"), f"got {out!r}"


def test_list_not_found_and_empty(list_exe):
    """list.c: a missing target is 'Not found'; an empty list prints 'List:' and 'Not found'"""
    out, _, _ = run(list_exe, "5\n9\n0\n7\n")
    assert "List: 9 5\n" in body(out) and body(out).rstrip().endswith("Not found"), f"got {out!r}"
    out, _, _ = run(list_exe, "0\n1\n")
    assert "List:\n" in body(out) and body(out).rstrip().endswith("Not found"), f"got {out!r}"


def test_list_valgrind_clean(list_exe):
    """list.c frees every node: valgrind reports no errors and no leaks"""
    need_valgrind()
    out, code, rep = run(list_exe, "4\n8\n15\n16\n23\n42\n0\n15\n", valgrind=True)
    assert code != 99 and "Invalid" not in rep, f"memory errors:\n{rep[:600]}"
    assert "definitely lost" not in rep, f"leak (missing free_list?):\n{rep[:600]}"
