---
week: 9
title: "Python: The Same Ideas in a Tenth of the Lines"
description: "Every C program you wrote, rewritten in Python: no types to declare, no semicolons, no memory to free, and a library for everything. What you gain, what you give up, and how to learn any new language in a day."
module: m4
status: draft
lab: lab-07
reading: "CS50 notes; Python tutorial chapters 3–5"
cs50:
  week: "6"
  title: "Python"
  video: "https://youtu.be/Rl0ludWTLxs"
  notes: "https://cs50.harvard.edu/x/2026/notes/6/"
  slides: "https://cdn.cs50.net/2025/fall/lectures/6/lecture6.pdf"
  source: "https://cdn.cs50.net/2025/fall/lectures/6/src6.zip"
  pset: "https://cs50.harvard.edu/x/2026/psets/6/"
prep:
  - "Watch the lecture and, for each program, write the C version in your head first. The point of the week is the comparison."
  - "Run <code>python3</code> in your codespace terminal and type <code>print(\"hello, world\")</code>. That is the whole setup."
objectives:
  - "Translate C programs with variables, conditions, loops and functions into Python."
  - "Use Python's built-in types: int, float, str, bool, list, dict, tuple, and explain dynamic typing."
  - "Handle input and exceptions with try/except and write input-validation loops."
  - "Import and use modules (random, csv, sys) and install packages with pip."
  - "Explain what an interpreter is, and why Python is slower than C but faster to write."
  - "Recognize when C is the right tool and when Python is."
wow:
  title: "CS50's speller: 200 lines of C become 20 lines of Python, and the Python version is still a hash table."
  text: "Python's set is a hash table written in C. Everything you built by hand in week 7 is one line: words = set(open('dictionary').read().split()). You did not waste week 7: you now know what that line costs and why it is fast. That is the difference between using a tool and understanding it, and it is the difference employers pay for."
industry:
  - { "t": "Python is the language of AI and data", "d": "PyTorch, TensorFlow, pandas, scikit-learn: every machine-learning system is driven from Python, while the heavy lifting runs in C and CUDA underneath." }
  - { "t": "Glue and automation", "d": "Most companies run thousands of Python scripts that move data, call APIs, generate reports and test systems. Knowing Python means never doing a repetitive task by hand again." }
  - { "t": "Interpreters and the speed trade-off", "d": "Instagram, YouTube and Dropbox run on Python, and each has rewritten hot paths in C or Rust. Knowing both is the actual industry skill." }
  - { "t": "pip and the supply chain", "d": "A one-line install pulls code written by strangers. The 2024 xz backdoor showed why professionals pin versions and read what they install." }
resources:
  - { "title": "CS50x 2026 · Week 6 notes", "url": "https://cs50.harvard.edu/x/2026/notes/6/" }
  - { "title": "The Python Tutorial (official)", "url": "https://docs.python.org/3/tutorial/", "note": "Chapters 3–5 cover this week." }
  - { "title": "CS50's Introduction to Programming with Python", "url": "https://cs50.harvard.edu/python/", "note": "A whole free course if you want more." }
tags: ["Python", "interpreter", "dynamic typing", "list", "dict", "exceptions", "modules", "pip"]
---

## Topics

1. **Hello, again**: `print("hello, world")`; running with `python3`; no compile step; the interpreter.
2. **Types without declarations**: `int`, `float`, `str`, `bool`; `input()` returns a string; `int(input())`; `try`/`except ValueError`.
3. **Conditions and loops**: indentation instead of braces; `if/elif/else`; `while`; `for i in range(n)`; `for c in s`.
4. **Lists and dicts**: `scores = [72, 73, 33]`, `sum(scores) / len(scores)`; `people = {"Carter": "+1-617"}`; the hash table from week 7, built in.
5. **Functions and modules**: `def`, default arguments, `import random`, `from cs50 import get_int`, `sys.argv`, `sys.exit`.
6. **Files**: `open`, `csv.reader`, `csv.DictWriter`.
7. **C versus Python**: overflow gone, floats still imprecise, speed 10–100× slower, and why that is usually fine.

Full notes are published before the lecture. The lab, [Lab 7: C to Python](/labs/lab-07), rewrites three earlier labs in Python and times the difference.
