---
lab: 2
week: 3
title: "C Kickstart"
description: "Your first real C programs: hello and a greeting that reads input, a byte printed as bits, then mario pyramids, a calculator with validated input, and cash change-making with a greedy loop."
assignment: lab02
status: draft
acceptUrl: ""
due: "2026-10-09 23:59"
duration: "90 min + finish at home"
points: 10
language: "C"
files: ["hello.c", "greet.c", "bits.c", "mario.c", "calculator.c", "cash.c"]
topics: ["compile", "printf", "get_string", "get_int", "do-while", "for loops", "functions"]
notebook: { file: "labs/templates/lab02/lab02.ipynb", title: "Lab 2 · Explore: C in a notebook" }
---

## Plan

This lab opens in week 3. The full step-by-step page and the tests are published before that Monday; the plan below is final.

1. **Warm-up (scaffolded, one line each)**: `hello.c` prints `hello, world`; `greet.c` reads a name with `get_string` and greets it; `bits.c` prints a number from 0–255 as 8 bits (the lecture's bit widget, in C).
2. **mario.c**: print a right-aligned pyramid of `#` of a height the user chooses (1–8), re-prompting on bad input.
3. **calculator.c**: read two integers and print sum, difference, product, quotient (as a float, two decimals) and remainder; handle division by zero.
4. **cash.c**: read an amount of change in cents and print the minimum number of coins (25, 10, 5, 1) with a greedy loop.
5. **Explore notebook**: C written, compiled and run inside Jupyter/Colab: types, `printf`, integer overflow on purpose.

The starter repository ships a mini CS50 library (`cs50.h`, `cs50.c`), a `Makefile` (`make hello`), and tests that compile your programs with `gcc` and run them.

## How it works

Same loop as every lab: accept on Classroom 50, open in Codespaces (gcc, make, gdb and valgrind are installed for you), solve the TODOs, `make program && ./program`, `python3 check.py` until green, `git push`. See [how labs work](/labs) and the [setup guide](/guides/lab-setup).
