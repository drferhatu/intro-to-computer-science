"""Shared helpers: run a Python program with stdin and arguments, capture its output."""
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent


def run(script: str, stdin: str = "", args=(), timeout: float = 60):
    path = ROOT / script
    if not path.exists():
        pytest.fail(f"{script} is missing")
    try:
        r = subprocess.run([sys.executable, str(path), *map(str, args)], input=stdin,
                           capture_output=True, text=True, timeout=timeout, cwd=ROOT)
    except subprocess.TimeoutExpired:
        pytest.fail(f"{script} did not finish in {timeout}s (an input loop that never ends?)")
    if r.returncode != 0 and "Traceback" in r.stderr:
        last = r.stderr.strip().splitlines()[-1]
        pytest.fail(f"{script} crashed: {last}")
    return r.stdout, r.returncode


def after_prompts(out: str) -> str:
    """Everything the program printed after the last prompt (prompts end with ': ' and no newline)."""
    lines = out.split("\n")
    first = lines[0]
    if ": " in first:
        first = first.rsplit(": ", 1)[1]
    lines[0] = first
    return "\n".join(lines).strip("\n")


def pyramid(h: int) -> str:
    return "\n".join(" " * (h - i - 1) + "#" * (i + 1) for i in range(h))
