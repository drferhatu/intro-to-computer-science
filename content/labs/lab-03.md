---
lab: 3
week: 4
title: "Strings and Ciphers"
description: "Arrays and strings under the hood: count letters and words, judge readability, and encrypt text with the Caesar cipher from the command line."
assignment: lab03
status: draft
acceptUrl: ""
due: "2026-10-18 23:59"
duration: "90 min + finish at home"
points: 10
language: "C"
files: ["scores.c", "readability.c", "caesar.c"]
topics: ["arrays", "strings", "ctype", "argc/argv", "exit codes"]
---

## Plan

This lab opens in week 4. The full step-by-step page, the starter repository and the tests are published before that Monday; the plan below is final.

1. **scores.c**: read N scores into an array and print min, max and average via functions that take the array.
2. **readability.c**: count letters, words and sentences in a text and print its Coleman–Liau grade.
3. **caesar.c**: `./caesar 13` reads plaintext and prints ciphertext; validate that the key is a positive integer, return 1 otherwise.
4. **Explore notebook**: what a string looks like byte by byte, and what happens when the `\\0` is missing.

## How it works

Same loop as every lab: accept on Classroom 50, open in Codespaces, solve the TODOs, `python3 check.py` until green, `git push`. See [how labs work](/labs) and the [setup guide](/guides/lab-setup).
