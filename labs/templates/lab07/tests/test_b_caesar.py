"""Part B"""
from conftest import run, after_prompts


def test_caesar_usage():
    """caesar.py prints the usage message and exits with 1 without a key, with two keys, or with a non-numeric key"""
    for args in [(), ("1", "2"), ("abc",), ("1x",)]:
        out, code = run("caesar.py", "", args)
        assert "Usage: python caesar.py key" in out, f"args {args}: expected the usage message, got {out!r}"
        assert code == 1, f"args {args}: expected exit status 1, got {code}"


def test_caesar_13():
    """caesar.py 13: HELLO, world → URYYB, jbeyq (case kept, punctuation unchanged)"""
    out, code = run("caesar.py", "HELLO, world\n", ("13",))
    assert code == 0
    assert after_prompts(out) == "URYYB, jbeyq", f"got {after_prompts(out)!r}"


def test_caesar_wrap_and_big_key():
    """caesar.py wraps around the alphabet and handles keys above 26"""
    out, _ = run("caesar.py", "xyz XYZ\n", ("3",))
    assert after_prompts(out) == "abc ABC", f"key 3 on 'xyz XYZ' → got {after_prompts(out)!r}"
    out, _ = run("caesar.py", "abc\n", ("27",))
    assert after_prompts(out) == "bcd", f"key 27 should act like 1, got {after_prompts(out)!r}"
    out, _ = run("caesar.py", "Firat 2026!\n", ("26",))
    assert after_prompts(out) == "Firat 2026!", f"key 26 should change nothing, got {after_prompts(out)!r}"


def test_caesar_label():
    """caesar.py labels its output with "ciphertext: " """
    out, _ = run("caesar.py", "a\n", ("1",))
    assert "ciphertext: b" in out, f"expected 'ciphertext: b' in the output, got {out!r}"
