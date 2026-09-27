---
lab: 5
week: 6
title: "Pointers and Pixels"
description: "Swap through pointers, copy a string by hand, allocate and free memory without leaks, and turn a color BMP image gray by editing its bytes."
assignment: lab05
status: draft
acceptUrl: ""
due: "2026-10-30 23:59"
duration: "90 min + finish at home"
points: 10
language: "C"
files: ["swap.c", "copy.c", "leaks.c", "filter.c"]
topics: ["pointers", "malloc/free", "valgrind", "strcpy", "file I/O", "BMP"]
---

## Plan

This lab opens in week 6. The full step-by-step page, the starter repository and the tests are published before that Monday; the plan below is final.

1. **swap.c**: a `swap(int *a, int *b)` that works, and a comment explaining why the by-value version cannot.
2. **copy.c**: copy a string with `malloc` and a loop, uppercase the copy, free it; valgrind must report no leaks.
3. **leaks.c**: a program with three deliberate memory errors that you find with valgrind and fix.
4. **filter.c**: grayscale and reflect filters on a 24-bit BMP, reading and writing the file with `fread`/`fwrite`.
5. **Explore notebook**: view the bytes of a BMP header with Python and check your C program's output pixel by pixel.

## How it works

Same loop as every lab: accept on Classroom 50, open in Codespaces, solve the TODOs, `python3 check.py` until green, `git push`. See [how labs work](/labs) and the [setup guide](/guides/lab-setup).
