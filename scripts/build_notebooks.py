#!/usr/bin/env python
"""Build the exploration notebooks and render them to HTML for the website.

- Writes each notebook from the cell definitions below (only if missing, unless --force).
- Optionally executes them (--execute) and renders public/notebooks/<name>.html (embedded on week and lab pages).
- C cells use `%%writefile` + `!clang`, so the notebooks run in Colab, in a codespace and in CI (clang required).

Usage:
  /opt/miniconda3/envs/ferhat_ml/bin/python scripts/build_notebooks.py [--execute] [--force]
"""
import sys
from pathlib import Path

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "public" / "notebooks"
SKIP_TAG = "skip-execution"
md = new_markdown_cell


def code(src, skip=False):
    c = new_code_cell(src)
    if skip:
        c.metadata["tags"] = [SKIP_TAG]
    return c


# ---------------------------------------------------------------------------
# WEEK 2 · bits, bytes, ASCII and pixels (Python)
# ---------------------------------------------------------------------------
WEEK02 = [
md("""# Week 2 · Explore: bits, bytes, ASCII and pixels

**Introduction to Computer Science (YMT113)** · Fall 2026

Nothing here is graded. Run each cell (`Shift+Enter`), read the output, change something, run it again.
Runs in Google Colab with nothing installed."""),
md("""## 1 · Counting in binary

Python can show any number in binary with `bin()` and pad it to 8 bits with `format`."""),
code("""for n in [0, 1, 2, 5, 73, 128, 255]:
    print(f"{n:>4}  →  {n:08b}")"""),
md("""Read each row from the left: 128 64 32 16 8 4 2 1. Add the place values under the 1s and you get the number back."""),
code("""bits = "01001001"
value = sum(int(b) * 2 ** (7 - i) for i, b in enumerate(bits))
print(bits, "=", value)"""),
md("""## 2 · Text is numbers: ASCII and Unicode

`ord()` gives a character's code, `chr()` goes back. ASCII is the first 128 codes; Unicode continues from there."""),
code("""for c in "Hi!":
    print(f"{c!r:5} {ord(c):4}  {ord(c):08b}")"""),
code("""print(chr(72), chr(105), chr(33))
print("Türkçe:", [ord(c) for c in "Şğü"])
print("😂 is code point", ord("😂"), "and takes", len("😂".encode("utf-8")), "bytes in UTF-8")"""),
md("""Your name as bytes:"""),
code("""name = "Firat"          # change me
data = name.encode("utf-8")
print(len(name), "characters →", len(data), "bytes →", 8 * len(data), "bits")
print(" ".join(f"{b:08b}" for b in data))"""),
md("""## 3 · The same bits, different meanings

Two bytes can be two letters, one 16-bit number, or part of a color. Bits carry no meaning; programs do."""),
code("""two = "Hi".encode("utf-8")
print("as text   :", two.decode("utf-8"))
print("as number :", int.from_bytes(two, "big"))
print("as color  : R =", two[0], " G =", two[1], " (with B = 0 →", f"#{two[0]:02x}{two[1]:02x}00)")"""),
md("""## 4 · An image is a grid of numbers

Each pixel is three bytes (red, green, blue). Let's draw a 8×8 smiley from a grid of 0/1 and then color it."""),
code("""import numpy as np
import matplotlib.pyplot as plt

smiley = np.array([
    [0,0,1,1,1,1,0,0],
    [0,1,0,0,0,0,1,0],
    [1,0,1,0,0,1,0,1],
    [1,0,0,0,0,0,0,1],
    [1,0,1,0,0,1,0,1],
    [1,0,0,1,1,0,0,1],
    [0,1,0,0,0,0,1,0],
    [0,0,1,1,1,1,0,0],
])
print(smiley)
plt.figure(figsize=(3, 3)); plt.imshow(smiley, cmap="gray_r"); plt.axis("off"); plt.show()"""),
code("""# now in color: every pixel is (R, G, B), 0–255
rgb = np.zeros((8, 8, 3), dtype=np.uint8)
rgb[smiley == 1] = (238, 90, 31)     # orange for the 1s
rgb[smiley == 0] = (246, 246, 242)   # paper for the 0s
print("one pixel:", rgb[0, 2], "→ 3 bytes")
print("whole image:", rgb.size, "bytes")
plt.figure(figsize=(3, 3)); plt.imshow(rgb); plt.axis("off"); plt.show()"""),
md("""A 1920×1080 photo is 2 073 600 pixels × 3 bytes ≈ 6.2 MB uncompressed. JPEG makes it ten times smaller by throwing away what your eye cannot see; that is an algorithm, next week's topic."""),
md("""## 5 · Why binary search wins

Count the steps needed to find one item among n, page by page (linear) and by halving (binary)."""),
code("""import math
print(f"{'n':>15} {'linear':>15} {'binary':>8}")
for n in [1_000, 1_000_000, 1_000_000_000, 8_000_000_000]:
    print(f"{n:>15,} {n:>15,} {math.ceil(math.log2(n)):>8}")"""),
md("""Eight billion people, 33 steps. That is the wow moment of week 5, seen from here."""),
]

# ---------------------------------------------------------------------------
# LAB 1 · C in a notebook
# ---------------------------------------------------------------------------
LAB01 = [
md("""# Lab 1 · Explore: C in a notebook

**Introduction to Computer Science (YMT113)** · Fall 2026

This notebook is the *playground* half of Lab 1. Nothing here is graded. It shows that you can write, compile and run **C** inside a
Jupyter notebook: a cell starting with `%%writefile hello.c` saves the cell as a file, and a cell starting with `!` runs a terminal command.

> Where to run it: in Google Colab (the **Open in Colab** button on the lab page; clang is preinstalled) or in your codespace (pick the Python kernel)."""),
md("""## 1 · hello, world"""),
code("""%%writefile hello.c
#include <stdio.h>

int main(void)
{
    printf("hello, world\\n");
}"""),
code("""!clang -o hello hello.c && ./hello"""),
md("""Two commands joined by `&&`: compile (`clang -o hello hello.c`), and if that worked, run (`./hello`). Try removing the semicolon and running both cells again: read the error the compiler gives you."""),
md("""## 2 · Types and printf

Change the values, run again. What happens if you print an `int` with `%f`?"""),
code("""%%writefile types.c
#include <stdio.h>

int main(void)
{
    int age = 19;
    float gpa = 3.75;
    char initial = 'F';
    printf("age %i, gpa %.2f, initial %c\\n", age, gpa, initial);
    printf("an int takes %zu bytes, a float %zu, a char %zu, a double %zu\\n",
           sizeof(int), sizeof(float), sizeof(char), sizeof(double));
}"""),
code("""!clang -o types types.c && ./types"""),
md("""## 3 · A byte as bits (the Part D program, explained)

`(n >> i) & 1` shifts the number right by `i` places and keeps only the last bit. Watch it work for one number:"""),
code("""%%writefile bits.c
#include <stdio.h>

int main(void)
{
    int n = 73;
    for (int i = 7; i >= 0; i--)
    {
        int bit = (n >> i) & 1;
        printf("i=%i  n>>i=%3i  bit=%i\\n", i, n >> i, bit);
    }
}"""),
code("""!clang -o bits bits.c && ./bits"""),
md("""## 4 · Integer overflow, on purpose

An `int` has 32 bits. What happens one past the largest value? (We meet this properly in week 3.)"""),
code("""%%writefile overflow.c
#include <stdio.h>
#include <limits.h>

int main(void)
{
    int big = INT_MAX;
    printf("largest int : %i\\n", big);
    big = big + 1;
    printf("plus one    : %i\\n", big);
    unsigned char byte = 255;
    byte = byte + 1;
    printf("255 + 1 in one byte: %i\\n", byte);
}"""),
code("""!clang -Wno-integer-overflow -o overflow overflow.c && ./overflow"""),
md("""The bits wrap around, like an odometer. This exact behavior grounded the Boeing 787 (week 3's wow moment).

## 5 · Your turn

Copy any cell, change the program, run it. Ideas: print your name and age; print 5 / 2 and 5.0 / 2; count from 1 to 10 with a `for` loop."""),
]

NOTEBOOKS = {
    "week-02-bits": (ROOT / "notebooks" / "week-02-bits.ipynb", WEEK02),
    "lab01": (ROOT / "labs" / "templates" / "lab01" / "lab01.ipynb", LAB01),
}


def build(path, cells, force=False):
    if path.exists() and not force:
        print(f"· {path.relative_to(ROOT)} exists, kept")
        return
    nb = new_notebook(cells=cells, metadata={
        "kernelspec": {"name": "python3", "display_name": "Python 3", "language": "python"},
        "language_info": {"name": "python"},
        "colab": {"name": path.name, "toc_visible": True},
    })
    path.parent.mkdir(parents=True, exist_ok=True)
    nbformat.write(nb, path)
    print(f"✓ {path.relative_to(ROOT)} written")


def execute(path):
    """Execute in a temporary directory so that C cells (%%writefile) never touch the starter files."""
    import tempfile
    from nbclient import NotebookClient
    nb = nbformat.read(path, as_version=4)
    with tempfile.TemporaryDirectory() as tmp:
        client = NotebookClient(nb, timeout=300, kernel_name="python3", allow_errors=True,
                                skip_cells_with_tag=SKIP_TAG, resources={"metadata": {"path": tmp}})
        client.execute()
    errs = [o for c in nb.cells if c.cell_type == "code" for o in c.get("outputs", []) if o.get("output_type") == "error"]
    print(f"✓ {path.name} executed ({len(errs)} error cells)")
    return nb


CSS = """<style>
  body{background:#fff !important;margin:0}
  .jp-Notebook{padding:16px 20px !important;max-width:100% !important}
  .jp-Cell{padding:0 !important}
  .jp-InputArea-editor{border-radius:10px;border:1px solid #dfe0d9}
  .jp-RenderedHTMLCommon{font-family:"Instrument Sans",system-ui,sans-serif;color:#101418}
  .jp-RenderedHTMLCommon table{font-size:13px}
</style></head>"""


def to_html(name, path, nb=None):
    from nbconvert import HTMLExporter
    exp = HTMLExporter(template_name="lab")
    exp.exclude_input_prompt = True
    exp.exclude_output_prompt = True
    body, _ = exp.from_notebook_node(nb) if nb is not None else exp.from_filename(str(path))
    body = body.replace("</head>", CSS, 1)
    out = OUT_DIR / f"{name}.html"
    out.write_text(body, encoding="utf-8")
    print(f"✓ {out.relative_to(ROOT)} ({len(body) // 1024} KB)")


def main():
    force = "--force" in sys.argv
    run = "--execute" in sys.argv
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for name, (path, cells) in NOTEBOOKS.items():
        build(path, cells, force)
        nb = execute(path) if run else None
        to_html(name, path, nb)


if __name__ == "__main__":
    main()
