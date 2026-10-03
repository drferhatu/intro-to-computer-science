"""Part A"""
from conftest import run


def test_hello(hello):
    """hello.c prints "hello, world" """
    out = run(hello)
    assert out == "hello, world\n", f"expected 'hello, world\\n', got {out!r}"
