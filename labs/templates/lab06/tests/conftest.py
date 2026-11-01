"""Shared helpers: compile, run (optionally under valgrind)."""
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
VALGRIND = shutil.which("valgrind")


def compile_c(name: str, sources) -> Path:
    exe = ROOT / name
    for s in sources:
        if not (ROOT / s).exists():
            pytest.fail(f"{s} is missing")
    r = subprocess.run(["gcc", "-std=c11", "-Wall", "-g", "-I", str(ROOT), "-o", str(exe), *[str(ROOT / s) for s in sources]],
                       capture_output=True, text=True, cwd=ROOT)
    if r.returncode != 0:
        first = next((l for l in r.stderr.splitlines() if "error" in l), r.stderr.strip().splitlines()[:1])
        pytest.fail(f"{name} does not compile: {first}")
    return exe


def run(exe: Path, stdin: str = "", args=(), timeout: float = 60, valgrind: bool = False):
    cmd = [str(exe), *map(str, args)]
    if valgrind:
        cmd = [VALGRIND, "--leak-check=full", "--error-exitcode=99", "-q", *cmd]
    try:
        r = subprocess.run(cmd, input=stdin, capture_output=True, text=True, timeout=timeout, cwd=ROOT)
    except subprocess.TimeoutExpired:
        pytest.fail(f"{exe.name} did not finish in {timeout}s (infinite loop in a list walk?)")
    return r.stdout, r.returncode, (r.stderr if valgrind else "")


def need_valgrind():
    if not VALGRIND:
        pytest.skip("valgrind is not installed here (the autograder and the codespace have it)")


@pytest.fixture(scope="session")
def list_exe():
    return compile_c("list", ["list.c", "cs50.c"])


@pytest.fixture(scope="session")
def queue_exe():
    return compile_c("queue", ["queue.c", "cs50.c"])


@pytest.fixture(scope="session")
def speller():
    # the official speller.c replaces the student's copy (grading uses this file)
    return compile_c("speller", ["speller.c", "dictionary.c"])
