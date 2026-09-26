---
lab: 4
week: 5
title: "Search and Sort"
description: "Implement linear and binary search and two sorting algorithms, then measure them: the first time you see Big O on a stopwatch."
assignment: lab04
status: draft
acceptUrl: ""
due: "2026-10-25 23:59"
duration: "90 min + finish at home"
points: 10
language: "C"
files: ["search.c", "sort.c", "timing.md"]
topics: ["linear search", "binary search", "selection sort", "bubble sort", "Big O", "structs"]
---

## Plan

This lab opens in week 5. The full step-by-step page, the starter repository and the tests are published before that Monday; the plan below is final.

1. **search.c**: linear and binary search over a sorted array of ints, returning the index or −1; a struct-based phone book searched by name.
2. **sort.c**: selection sort and bubble sort; print the array after each pass so you can see them work.
3. **timing.md**: time both sorts on 1 000, 10 000 and 50 000 random numbers and fill in a table; explain the shape with Big O.
4. **Explore notebook**: merge sort in Python with a step counter, compared with your C timings.

## How it works

Same loop as every lab: accept on Classroom 50, open in Codespaces, solve the TODOs, `python3 check.py` until green, `git push`. See [how labs work](/labs) and the [setup guide](/guides/lab-setup).
