"""Part D"""
from pathlib import Path
from conftest import run, read_bmp, ROOT

IMAGES = ROOT / "images"


def gray(rows):
    return [[(round((r + g + b) / 3),) * 3 for (r, g, b) in row] for row in rows]


def mirror(rows):
    return [row[::-1] for row in rows]


def apply(filter_exe, mode, name):
    out = IMAGES / f"out-test-{mode}-{name}"
    if out.exists():
        out.unlink()
    stdout, code, _ = run(filter_exe, "", (mode, str(IMAGES / name), str(out)))
    assert code == 0, f"./filter {mode} exited with {code}: {stdout!r}"
    return read_bmp(out)


def test_grayscale(filter):
    """grayscale: every pixel becomes the rounded average of its r, g, b (tiny.bmp and firat.bmp)"""
    for name in ("tiny.bmp", "firat.bmp"):
        assert apply(filter, "grayscale", name) == gray(read_bmp(IMAGES / name)), f"grayscale wrong on {name}"


def test_reflect(filter):
    """reflect: every row is mirrored (tiny.bmp has padding, smiley.bmp does not)"""
    for name in ("tiny.bmp", "smiley.bmp"):
        assert apply(filter, "reflect", name) == mirror(read_bmp(IMAGES / name)), f"reflect wrong on {name}"


def test_reflect_twice_is_identity(filter):
    """reflecting twice gives the original image back"""
    src = read_bmp(IMAGES / "firat.bmp")
    once = IMAGES / "out-test-reflect-firat.bmp"
    run(filter, "", ("reflect", str(IMAGES / "firat.bmp"), str(once)))
    assert read_bmp(once) != src, "reflect changed nothing: the gradient image is not symmetric"
    twice = IMAGES / "out-test-reflect2-firat.bmp"
    run(filter, "", ("reflect", str(once), str(twice)))
    assert read_bmp(twice) == src
