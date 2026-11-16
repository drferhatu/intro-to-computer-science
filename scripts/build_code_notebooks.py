#!/usr/bin/env python
"""Make a one-program Colab notebook for every Python lecture program, so that each code box on a
week page can offer "Open in Colab".

  public/c/week-NN/name.py  →  notebooks/code/week-NN/name.ipynb

  /opt/miniconda3/envs/ferhat_ml/bin/python scripts/build_code_notebooks.py

How a program is turned into a notebook:
  - ordinary programs go into one code cell and run there (input() and charts work in Colab);
  - programs that read the command line (sys.argv) or call sys.exit are written to a file with
    %%writefile and run with `!python name.py <example arguments>`, exactly as in a terminal;
  - a setup cell installs the libraries Colab does not ship (cs50, cowsay, qrcode, python-dotenv) and
    downloads the files the program reads (scores.csv, convert.py, ...) from the course site.
Per-program details (arguments, extra files, a cell that shows the result) are in EXTRA below.
Run it again after adding or changing a lecture program; commit the notebooks (Colab opens them from GitHub).
"""
import json
import re
from pathlib import Path

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "public" / "c"
OUT = ROOT / "notebooks" / "code"
COURSE = json.loads((ROOT / "content" / "data" / "course.json").read_text(encoding="utf-8"))
SITE = "https://drferhatu.github.io/intro-to-computer-science"

# import name → pip package, for what Colab does not preinstall
PIP = {"cs50": "cs50", "cowsay": "cowsay", "qrcode": "qrcode[pil]", "dotenv": "python-dotenv"}

# (week, file) → args: command-line arguments for the example run (forces "script" mode)
#                 mode: "cell" | "script" (overrides the automatic choice)
#                 files: other files of the same week the program needs
#                 before / after: extra shell or Python lines run before / after the program
#                 run: the command used instead of `python name.py args`
#                 note: one sentence shown above the program
EXTRA = {
    ("week-08", "greet.py"): {"args": "Ferhat"},
    ("week-08", "exit.py"): {"args": "Ferhat", "after": ["!python exit.py; echo \"exit status: $?\""]},
    ("week-08", "grades.py"): {"args": "scores.csv", "before": ["%%writefile scores.csv\nname,lab1,lab2,lab3\nMario,10,9,8\nLuigi,7,10,9\nPeach,10,10,10"]},
    ("week-08", "survey.py"): {"before": ["%%writefile answers.csv\nlanguage\nPython\nC\nPython\nJava\nPython\nC\nJavaScript\nPython"]},
    ("week-08", "save0.py"): {"after": ["!cat phonebook.csv"]},
    ("week-08", "save1.py"): {"after": ["!cat phonebook.csv"]},
    ("week-08", "save2.py"): {"before": ["!echo 'name,number' > phonebook.csv"], "after": ["!cat phonebook.csv"]},
    ("week-08", "qr.py"): {"after": ["from IPython.display import Image\nImage(\"qr.png\")"],
                           "note": "The last line of the program, `os.system(\"open qr.png\")`, opens the image on a Mac; in Colab it does nothing, so the cell after the program shows the picture instead."},
    ("week-08", "blur.py"): {"files": ["bridge.bmp"], "after": ["from PIL import Image\ndisplay(Image.open(\"bridge.bmp\"), Image.open(\"out.bmp\"))"]},
    ("week-08", "edges.py"): {"files": ["bridge.bmp"], "after": ["from PIL import Image\ndisplay(Image.open(\"bridge.bmp\"), Image.open(\"out.bmp\"))"]},
    ("week-08", "speller.py"): {"args": "dictionaries/small texts/cat.txt", "files": ["dictionary.py", "dictionaries/small", "texts/cat.txt"]},
    ("week-08", "dictionary.py"): {"note": "This file is a module: it only defines functions, so running it prints nothing. `speller.py` imports it; the last cell tries the functions by hand.",
                                  "files": ["dictionaries/small"], "after": ["print(load(\"dictionaries/small\"), size(), check(\"Cat\"), check(\"purrs\"))"]},
    ("week-08", "integer1.py"): {"note": "Type `cat` to see the crash this program is here to show: a `ValueError` traceback."},
    ("week-09", "api1.py"): {"mode": "cell"},
    ("week-09", "main.py"): {"args": "21.5", "files": ["convert.py"]},
    ("week-09", "convert.py"): {"note": "This file is a module: it only defines functions, so running it prints nothing. The last cell calls them.",
                                "after": ["print(celsius_to_fahrenheit(100), describe(21.5))"]},
    ("week-09", "test_convert.py"): {"mode": "script", "files": ["convert.py"], "run": "!python -m pytest -q test_convert.py"},
    ("week-09", "keys.py"): {"before": ["!echo 'API_KEY=abc123' > .env"],
                             "note": "The setup cell creates a `.env` file with a made-up key, as you would on your own computer. Never do this with a real key in a notebook you share."},
}
# every program of these weeks reads this file
WEEK_FILES = {"week-09": {"table": ["scores.csv"], "chart": ["scores.csv"]}}


def needs_script(code):
    return bool(re.search(r"\bargv\b|sys\.exit\(", code))


def build(week, path):
    code = path.read_text(encoding="utf-8").rstrip() + "\n"
    name = path.name
    x = EXTRA.get((week, name), {})
    mode = x.get("mode") or ("script" if ("args" in x or needs_script(code)) else "cell")
    files = list(x.get("files", []))
    for prefix, extra in WEEK_FILES.get(week, {}).items():
        if name.startswith(prefix):
            files += extra
    pips = sorted({PIP[m] for m in re.findall(r"^(?:import|from)\s+(\w+)", code, re.M) if m in PIP})

    n = int(week.split("-")[1])
    cells = [new_markdown_cell(
        f"# {name}\n\n**Introduction to Computer Science (YMT113)** · Week {n} · "
        f"[back to the week page]({SITE}/weeks/{week}/)\n\n"
        "Run each cell with **Shift+Enter**, top to bottom. Change the code and run it again: this copy is yours."
        + (f"\n\n> {x['note']}" if x.get("note") else ""))]

    setup = []
    if pips:
        setup.append("!pip install -q " + " ".join(f"'{p}'" if "[" in p else p for p in pips))
    for f in files:
        folder = f"-P {Path(f).parent} " if "/" in f else ""
        setup.append(f"!wget -q -nc {folder}{SITE}/c/{week}/{f}")
    if setup:
        cells += [new_markdown_cell("## Setup\n\nInstalls what Colab does not have and fetches the files this program reads. Run it once."),
                  new_code_cell("\n".join(setup))]
    for b in x.get("before", []):
        cells.append(new_code_cell(b))

    if mode == "cell":
        cells += [new_markdown_cell("## The program"), new_code_cell(code.rstrip())]
    else:
        run = x.get("run") or f"!python {name} {x.get('args', '')}".rstrip()
        cells += [new_markdown_cell(f"## The program\n\nThis program reads the command line, so it is saved as a file first (`%%writefile`) and then run as in a terminal."),
                  new_code_cell(f"%%writefile {name}\n{code.rstrip()}"),
                  new_markdown_cell("## Run it\n\nChange the arguments after the file name and run again."),
                  new_code_cell(run)]
    for a in x.get("after", []):
        cells.append(new_code_cell(a))

    nb = new_notebook(cells=cells, metadata={
        "kernelspec": {"name": "python3", "display_name": "Python 3", "language": "python"},
        "language_info": {"name": "python"},
        "colab": {"name": f"{week}-{path.stem}.ipynb"},
    })
    out = OUT / week / f"{path.stem}.ipynb"
    out.parent.mkdir(parents=True, exist_ok=True)
    text = nbformat.writes(nb)
    # stable cell ids, so that an unchanged program gives an unchanged file
    ids = iter(range(10_000))
    text = re.sub(r'"id": "[0-9a-f]+"', lambda m: f'"id": "c{next(ids):03d}"', text)
    if not out.exists() or out.read_text(encoding="utf-8") != text:
        out.write_text(text, encoding="utf-8")
        return 1
    return 0


def main():
    changed = total = 0
    for week_dir in sorted(SRC.glob("week-*")):
        for path in sorted(week_dir.glob("*.py")):
            changed += build(week_dir.name, path)
            total += 1
    print(f"✓ {total} program notebooks in {OUT.relative_to(ROOT)} ({changed} written)")


if __name__ == "__main__":
    main()
