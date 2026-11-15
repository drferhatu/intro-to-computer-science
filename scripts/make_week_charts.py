#!/usr/bin/env python
"""Run the chart programs of a lecture week and save what plt.show() would display as PNGs for the week page.

  /opt/miniconda3/envs/ferhat_ml/bin/python scripts/make_week_charts.py week-09 chart0 chart1 chart2 chart3 api2

Each program runs inside public/c/<week>/ (so relative data files resolve) with plt.show() replaced by
savefig → public/img/<week>/<program>.png. Files the programs write themselves are removed afterwards.
"""
import os
import runpy
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent


def main():
    week, programs = sys.argv[1], sys.argv[2:]
    src = ROOT / "public" / "c" / week
    out = ROOT / "public" / "img" / week
    out.mkdir(parents=True, exist_ok=True)
    before = set(src.iterdir())
    os.chdir(src)
    plt.rcParams.update({"figure.figsize": (7, 3.8), "font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    for name in programs:
        target = out / f"{name}.png"
        plt.show = lambda *a, t=target, **k: (plt.savefig(t, dpi=140, bbox_inches="tight"), plt.close("all"))
        runpy.run_path(str(src / f"{name}.py"), run_name="__main__")
        print(f"✓ {target.relative_to(ROOT)}")
    for extra in set(src.iterdir()) - before:
        if extra.is_file():
            extra.unlink()


if __name__ == "__main__":
    main()
