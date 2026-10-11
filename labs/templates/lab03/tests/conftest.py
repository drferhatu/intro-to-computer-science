"""Shared helpers for the lab tests: compile a C file once, run it with input and arguments."""
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent


def compile_c(name: str) -> Path:
    exe = ROOT / name
    src = ROOT / f"{name}.c"
    if not src.exists():
        pytest.fail(f"{name}.c is missing")
    r = subprocess.run(["gcc", "-std=c11", "-Wall", "-I", str(ROOT), "-o", str(exe), str(src), str(ROOT / "cs50.c"), "-lm"],
                       capture_output=True, text=True, cwd=ROOT)
    if r.returncode != 0:
        first = next((l for l in r.stderr.splitlines() if "error" in l), r.stderr.strip().splitlines()[:1])
        pytest.fail(f"{name}.c does not compile: {first}")
    return exe


def run(exe: Path, stdin: str = "", args=(), timeout: float = 5):
    """Run a compiled program; returns (stdout, exit code)."""
    try:
        r = subprocess.run([str(exe), *map(str, args)], input=stdin, capture_output=True, text=True, timeout=timeout, cwd=ROOT)
    except subprocess.TimeoutExpired:
        pytest.fail(f"{exe.name} did not finish in {timeout}s (is it waiting for input, or stuck in a loop?)")
    return r.stdout, r.returncode


def after_prompts(out: str) -> str:
    """Everything printed after the last prompt (prompts end with ': ' or '? ' and no newline)."""
    lines = out.split("\n")
    first = lines[0]
    for sep in (": ", "? "):
        if sep in first:
            first = first.rsplit(sep, 1)[1]
    return "\n".join([first] + lines[1:]).strip("\n")


for _n in ["scores", "readability", "caesar"]:
    globals()[_n] = pytest.fixture(scope="session", name=_n)(lambda _n=_n: compile_c(_n))
