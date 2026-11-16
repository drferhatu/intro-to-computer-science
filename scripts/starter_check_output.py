#!/usr/bin/env python
"""Print what `python3 check.py` shows on the untouched starter of a lab, in full, for the lab page.

  /opt/miniconda3/envs/ferhat_ml/bin/python scripts/starter_check_output.py lab07

Runs the lab's tests on a temporary copy of labs/templates/<lab>. Tests that are skipped on this machine
(valgrind is Linux-only) are listed as failing, because the codespace and the autograder do run them.
"""
import shutil
import sys
import tempfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent


class Reporter:
    def __init__(self):
        self.items, self.lines, self.seen = [], {}, set()

    def pytest_collection_modifyitems(self, items):
        self.items = list(items)

    def pytest_runtest_logreport(self, report):
        if report.nodeid in self.seen:
            return
        if report.when == "call" or (report.when == "setup" and report.outcome != "passed"):
            self.seen.add(report.nodeid)
            item = next(i for i in self.items if i.nodeid == report.nodeid)
            doc = (item.function.__doc__ or item.name).strip().splitlines()[0]
            if report.passed:
                self.lines[report.nodeid] = f":) {doc}"
            elif report.skipped:
                self.lines[report.nodeid] = f":( {doc}"
            else:
                msg = str(report.longrepr.reprcrash.message) if hasattr(report.longrepr, "reprcrash") else str(report.longrepr)
                hint = msg.split("\n")[0].replace("AssertionError: ", "").replace("Failed: ", "")
                mark = ":|" if "does not compile" in hint or "missing" in hint else ":("
                self.lines[report.nodeid] = f"{mark} {doc}\n    {hint[:300]}"


def main():
    lab = sys.argv[1]
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t) / lab
        shutil.copytree(ROOT / "labs" / "templates" / lab, tmp)
        r = Reporter()
        import os
        os.chdir(tmp)
        sys.path.insert(0, str(tmp / "tests"))
        pytest.main(["-p", "no:terminal", "-p", "no:cacheprovider", "tests"], plugins=[r])
    passed = sum(1 for l in r.lines.values() if l.startswith(":)"))
    for item in r.items:
        print(r.lines.get(item.nodeid, f":( {item.name}"))
    print(f"\n{passed}/{len(r.items)} checks passed")


if __name__ == "__main__":
    main()
