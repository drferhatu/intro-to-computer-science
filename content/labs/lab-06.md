---
lab: 6
week: 7
title: "Build a Hash Table"
description: "From a linked list to a hash table for a word list: insert, search, size, unload, all valgrind-clean, then measure lookup time against a plain array."
assignment: lab06
status: draft
acceptUrl: ""
due: "2026-11-06 23:59"
duration: "90 min + finish at home"
points: 10
language: "C"
files: ["list.c", "dictionary.c", "dictionary.h"]
topics: ["linked list", "hash table", "hash function", "valgrind", "trade-offs"]
---

## Plan

This lab opens in week 7. The full step-by-step page, the starter repository and the tests are published before that Monday; the plan below is final.

1. **list.c**: a singly linked list of ints: insert at head, print, search, free.
2. **dictionary.c**: `load`, `check`, `size`, `unload` for a dictionary file, using an array of linked lists and a hash function you design.
3. **Benchmark**: a provided `speller` driver times your table on a 140 000-word dictionary; compare two hash functions.
4. **Explore notebook**: distribution of words across buckets drawn as a bar chart for each hash function.

## How it works

Same loop as every lab: accept on Classroom 50, open in Codespaces, solve the TODOs, `python3 check.py` until green, `git push`. See [how labs work](/labs) and the [setup guide](/guides/lab-setup).
