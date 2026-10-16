#!/usr/bin/env python
"""Assign the semester projects and publish them as encrypted cards.

Privacy: the site never contains names, numbers or readable project assignments. Each card
(project title, scopes, masked name, GitHub username) is encrypted with AES-256-GCM under a key
derived from the student's number with PBKDF2 (same parameters as src/pages/project.astro).
A student types their number on /project; the browser derives the same key and can open only
their own card. "View source" shows ciphertext only.

Assignment is random but reproducible (SEED). 22 students, 20 projects: the two projects that
are given twice get different advanced scopes (variant A / B). OVERRIDES pins a student to a project.

Outputs:
  content/data/project-cards.json       encrypted cards (published)
  private/project-assignments.json      clear list, instructor only (git-ignored)
  private/project-messages.md           one personal message per student, ready to paste

Usage:
  /opt/miniconda3/envs/ferhat_ml/bin/python scripts/assign_projects.py
"""
import base64
import csv
import hashlib
import json
import os
import random
from pathlib import Path

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

ROOT = Path(__file__).resolve().parent.parent
ROSTER = ROOT / "private" / "roster" / "ymt113-roster.csv"
BANK = ROOT / "private" / "project-ideas.json"
OUT = ROOT / "content" / "data" / "project-cards.json"
SALT = "YMT113-2026"      # must match src/pages/project.astro
KDF_ITER = 300_000        # must match src/pages/project.astro
SEED = 20261019
OVERRIDES: dict[str, str] = {}   # {"250543001": "P07"}
# projects that may be given to two students, with a different emphasis for the second one
DOUBLE_OK = {
    "P07": ("Image filters: grayscale, sepia, reflect, blur + Sobel edges (variant A)",
            "Image filters: grayscale, sepia, reflect, blur + pixelate/mosaic and ASCII-art export (variant B)"),
    "P14": ("Unbeatable tic-tac-toe in C, then Connect Four with alpha-beta (variant A)",
            "Unbeatable tic-tac-toe in Python, then a 4×4 board with depth-limited minimax and a node counter (variant B)"),
}


def mask(name: str) -> str:
    return " ".join(p[0] + "*" * max(len(p) - 1, 1) for p in name.split())


def key_for(number: str) -> bytes:
    return hashlib.pbkdf2_hmac("sha256", number.encode(), SALT.encode(), KDF_ITER, dklen=32)


def encrypt(payload: dict, number: str) -> dict:
    iv = os.urandom(12)
    ct = AESGCM(key_for(number)).encrypt(iv, json.dumps(payload, ensure_ascii=False).encode(), None)
    return {"iv": base64.b64encode(iv).decode(), "ct": base64.b64encode(ct).decode()}


def main():
    students = sorted(csv.DictReader(open(ROSTER, encoding="utf-8")), key=lambda r: r["email"])
    bank = json.loads(BANK.read_text(encoding="utf-8"))
    projects = [dict(p, theme=t["title"], weeks=t["weeks"]) for t in bank["themes"] for p in t["projects"]]
    by_id = {p["id"]: p for p in projects}

    rng = random.Random(SEED)
    pool = [p["id"] for p in projects if p["id"] not in OVERRIDES.values()]
    rng.shuffle(pool)
    extra = [pid for pid in DOUBLE_OK if pid not in OVERRIDES.values()]
    need = len(students) - len(OVERRIDES) - len(pool)
    if need > len(extra):
        raise SystemExit(f"{len(students)} students, {len(projects)} projects: add more DOUBLE_OK entries")
    queue = pool + extra[:need]

    cards, clear, msgs = [], [], []
    given: dict[str, int] = {}
    for s in students:
        no = s["email"].split("@")[0]
        name = f"{s['first_name']} {s['last_name']}"
        pid = OVERRIDES.get(no) or queue.pop(0)
        p = by_id[pid]
        given[pid] = given.get(pid, 0) + 1
        variant = ""
        if pid in DOUBLE_OK:
            variant = DOUBLE_OK[pid][given[pid] - 1]
        card = {
            "code": pid, "title": p["title"], "theme": p["theme"], "lang": p["lang"], "difficulty": p["difficulty"],
            "weeks": p["weeks"], "summary": p["summary"], "core": p["core"], "min": p["min"], "advanced": p["advanced"],
            "variant": variant, "student": mask(name), "github": s["username"],
            "repo": f"introduction-to-computer-science-project-{s['username']}",
        }
        cards.append({"id": f"{pid}-{given[pid]}", **encrypt(card, no)})
        clear.append({"student_id": no, "name": name, "github": s["username"], **card})
        msgs.append(f"""### {name} ({no}, @{s['username']})

Hi {s['first_name']},

your semester project is **{pid} · {p['title']}** ({p['lang']}, theme: {p['theme']}).
{p['summary']}

- Minimum scope: {p['min']}
- Advanced scope: {p['advanced']}{(chr(10) + '- Your variant: ' + variant) if variant else ''}

Open https://drferhatu.github.io/intro-to-computer-science/project, type your student number and you will see this card with the milestones. Accept the project repository on Classroom 50 (button on the same page), write a one-paragraph plan and a task list in the README, and make your first commit this week.

Ferhat Uçar
""")
        print(f"{pid}  {name:28s} {s['username']:26s} {p['title']}{'  [' + variant[:9] + '…]' if variant else ''}")

    OUT.write_text(json.dumps({"salt": SALT, "iter": KDF_ITER, "cards": cards}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / "private" / "project-assignments.json").write_text(json.dumps(clear, ensure_ascii=False, indent=2), encoding="utf-8")
    (ROOT / "private" / "project-messages.md").write_text("\n".join(msgs), encoding="utf-8")
    print(f"\n✓ {OUT.relative_to(ROOT)} ({len(cards)} encrypted cards)\n✓ private/project-assignments.json, private/project-messages.md")


if __name__ == "__main__":
    main()
