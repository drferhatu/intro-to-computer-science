"""Shared helpers for the lab tests: compile a C file once, run it with input."""
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent


def compile_c(name: str) -> Path:
    """Compile <name>.c together with cs50.c into ./<name>. Fails the test with the compiler output."""
    exe = ROOT / name
    src = ROOT / f"{name}.c"
    if not src.exists():
        pytest.fail(f"{name}.c is missing")
    r = subprocess.run(["gcc", "-std=c11", "-Wall", "-I", str(ROOT), "-o", str(exe), str(src), str(ROOT / "cs50.c")],
                       capture_output=True, text=True, cwd=ROOT)
    if r.returncode != 0:
        first = next((l for l in r.stderr.splitlines() if "error" in l), r.stderr.strip().splitlines()[:1])
        pytest.fail(f"{name}.c does not compile: {first}")
    return exe


def run(exe: Path, stdin: str = "", timeout: float = 5) -> str:
    """Run a compiled program with the given input and return its stdout."""
    try:
        r = subprocess.run([str(exe)], input=stdin, capture_output=True, text=True, timeout=timeout, cwd=ROOT)
    except subprocess.TimeoutExpired:
        pytest.fail(f"{exe.name} did not finish in {timeout}s (is it waiting for input, or stuck in a loop?)")
    return r.stdout


@pytest.fixture(scope="session")
def hello():
    return compile_c("hello")


@pytest.fixture(scope="session")
def greet():
    return compile_c("greet")


@pytest.fixture(scope="session")
def bits():
    return compile_c("bits")
