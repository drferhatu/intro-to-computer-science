"""Shared helpers: compile a C file, run it (optionally under valgrind), read BMP pixels."""
import shutil
import struct
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
VALGRIND = shutil.which("valgrind")


def compile_c(name: str) -> Path:
    exe, src = ROOT / name, ROOT / f"{name}.c"
    if not src.exists():
        pytest.fail(f"{name}.c is missing")
    r = subprocess.run(["gcc", "-std=c11", "-Wall", "-g", "-I", str(ROOT), "-o", str(exe), str(src), str(ROOT / "cs50.c"), "-lm"],
                       capture_output=True, text=True, cwd=ROOT)
    if r.returncode != 0:
        first = next((l for l in r.stderr.splitlines() if "error" in l), r.stderr.strip().splitlines()[:1])
        pytest.fail(f"{name}.c does not compile: {first}")
    return exe


def run(exe: Path, stdin: str = "", args=(), timeout: float = 20, valgrind: bool = False):
    """Run a program; returns (stdout, exit code, valgrind report or '')."""
    cmd = [str(exe), *map(str, args)]
    if valgrind:
        cmd = [VALGRIND, "--leak-check=full", "--error-exitcode=99", "-q", *cmd]
    try:
        r = subprocess.run(cmd, input=stdin, capture_output=True, text=True, timeout=timeout, cwd=ROOT)
    except subprocess.TimeoutExpired:
        pytest.fail(f"{exe.name} did not finish in {timeout}s")
    return r.stdout, r.returncode, (r.stderr if valgrind else "")


def need_valgrind():
    if not VALGRIND:
        pytest.skip("valgrind is not installed here (the autograder and the codespace have it)")


def after_prompts(out: str) -> str:
    lines = out.split("\n")
    first = lines[0]
    if ": " in first:
        first = first.rsplit(": ", 1)[1]
    return "\n".join([first] + lines[1:]).strip("\n")


def read_bmp(path: Path):
    """Return rows top→bottom of (r, g, b) tuples."""
    data = path.read_bytes()
    assert data[:2] == b"BM", f"{path.name} is not a BMP"
    off = struct.unpack_from("<I", data, 10)[0]
    w, h = struct.unpack_from("<ii", data, 18)
    pad = (4 - (w * 3) % 4) % 4
    rows = []
    p = off
    for _ in range(abs(h)):
        row = []
        for _ in range(w):
            b, g, r = data[p], data[p + 1], data[p + 2]
            row.append((r, g, b)); p += 3
        rows.append(row); p += pad
    return rows[::-1] if h > 0 else rows


for _n in ["swap", "copy", "leaks", "filter"]:
    globals()[_n] = pytest.fixture(scope="session", name=_n)(lambda _n=_n: compile_c(_n))
