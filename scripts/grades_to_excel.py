#!/usr/bin/env python
"""Turn the Classroom 50 scores.json of one lab into a formatted Excel grade sheet for the whole roster.

  1. fetch <org>/classroom50/<classroom>/scores.json (run "Collect now" / the Collect Scores workflow first),
  2. for every student on private/roster/ymt113-roster.csv pick the last submission that is at most
     --late-days after the deadline (read from the lab page), apply 10% per late day,
  3. write private/grades/YMT113_LabN_Notlar.xlsx with per-part points.

Usage:
  /opt/miniconda3/envs/ferhat_ml/bin/python scripts/grades_to_excel.py lab04 [--late-days 5] [--points 10]
"""
import argparse, base64, csv, json, math, re, subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill

ROOT = Path(__file__).resolve().parent.parent
COURSE = json.loads((ROOT / "content" / "data" / "course.json").read_text(encoding="utf-8"))
ORG, CLS = COURSE["classroom"]["org"], COURSE["classroom"]["slug"]
TZ = timezone(timedelta(hours=3))


def lab_meta(slug):
    for p in sorted((ROOT / "content" / "labs").glob("*.md*")):
        fm = p.read_text(encoding="utf-8").split("---")[1]
        if re.search(rf"^assignment:\s*{slug}\s*$", fm, re.M):
            due = re.search(r'^due:\s*"?(\d{4}-\d\d-\d\d \d\d:\d\d)"?', fm, re.M).group(1)
            n = int(re.search(r"^lab:\s*(\d+)", fm, re.M).group(1))
            title = re.search(r'^title:\s*"(.*)"', fm, re.M).group(1)
            return n, title, due
    raise SystemExit(f"no lab page with assignment {slug}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug"); ap.add_argument("--late-days", type=int, default=5); ap.add_argument("--points", type=float, default=10)
    a = ap.parse_args()
    n, title, due_s = lab_meta(a.slug)
    due = datetime.strptime(due_s, "%Y-%m-%d %H:%M").replace(tzinfo=TZ)
    raw = subprocess.run(["gh", "api", f"repos/{ORG}/classroom50/contents/{CLS}/scores.json", "--jq", ".content"], capture_output=True, text=True, check=True).stdout
    entries = json.loads(base64.b64decode(raw))["assignments"][a.slug]["entries"]
    by_user = {e["owner"].lower(): e for e in entries}
    roster = sorted(csv.DictReader(open(ROOT / "private" / "roster" / "ymt113-roster.csv", encoding="utf-8")), key=lambda r: r["email"])
    parts = []
    for e in entries:
        for s in e.get("submissions", []):
            for t in s["tests"]:
                if t["test-name"] not in parts: parts.append(t["test-name"])
    parts.sort()

    wb = openpyxl.Workbook(); ws = wb.active; ws.title = f"Lab {n}"
    ws.append(["#", "Öğrenci No", "Ad Soyad", "GitHub", "Son teslim (TR)", "Geç gün", f"Puan ({a.points:g})", "Kesintili puan"] + [p.split("·")[0].strip() + " " + p.split("·")[-1].strip() for p in parts] + ["Not"])
    scores = []
    for i, r in enumerate(roster, 1):
        no = r["email"].split("@")[0]; name = f"{r['first_name']} {r['last_name']}"
        e = by_user.get(r["username"].lower())
        if not e or not e.get("submissions"):
            ws.append([i, no, name, r["username"], "", "", 0, 0] + [0] * len(parts) + ["Teslim yok" if not e else "Kabul etti, push yok"]); continue
        subs = sorted(e["submissions"], key=lambda s: s["datetime"])
        ok = [s for s in subs if datetime.strptime(s["datetime"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc) <= due + timedelta(days=a.late_days)]
        s = ok[-1] if ok else subs[-1]
        when = datetime.strptime(s["datetime"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).astimezone(TZ)
        late = max(0, math.ceil((when - due).total_seconds() / 86400))
        adj = round(s["score"] * max(0, 1 - 0.1 * late), 2); scores.append(adj)
        t = {x["test-name"]: x["score"] for x in s["tests"]}
        ws.append([i, no, name, r["username"], when.strftime("%Y-%m-%d %H:%M"), late, s["score"], adj] + [t.get(p, 0) for p in parts] + [f"{late} gün geç, %{late*10} kesinti" if late else ""])
    ws.append([]); ws.append(["", "", f"Ortalama ({len(scores)} teslim / {len(roster)} öğrenci)", "", "", "", "", round(sum(scores) / len(scores), 2) if scores else 0])
    bold, fill = Font(bold=True), PatternFill("solid", fgColor="D9EEF0")
    for c in ws[1]: c.font = bold; c.fill = fill; c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    widths = [4, 12, 26, 24, 17, 8, 9, 12] + [9] * len(parts) + [30]
    for col, w in enumerate(widths, 1): ws.column_dimensions[openpyxl.utils.get_column_letter(col)].width = w
    note_col = 8 + len(parts) + 1
    for row in ws.iter_rows(min_row=2, max_row=len(roster) + 1):
        for c in row:
            if c.column not in (3, 4, note_col): c.alignment = Alignment(horizontal="center")
        if row[note_col - 1].value in ("Teslim yok", "Kabul etti, push yok"):
            for c in row: c.fill = PatternFill("solid", fgColor="FBE3E3")
    ws.freeze_panes = "A2"
    out = ROOT / "private" / "grades" / f"YMT113_Lab{n}_Notlar.xlsx"; wb.save(out)
    print(f"✓ {out.relative_to(ROOT)} · {title} · due {due_s} · {len(scores)} submitted / {len(roster)} · mean {round(sum(scores)/len(scores), 2) if scores else 0}")
    for row in ws.iter_rows(min_row=2, max_row=len(roster) + 1, values_only=True):
        print(f"  {row[2]:26} {str(row[7]):>5}  {row[note_col-1] or ''}")


if __name__ == "__main__":
    main()
