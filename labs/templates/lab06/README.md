# Lab 6 · Build a Hash Table

Introduction to Computer Science (YMT113) · Fall 2026 · Fırat University

## Student

<!-- Fill in both lines, then commit. -->
- Name:
- Student ID:

**Full instructions:** https://drferhatu.github.io/intro-to-computer-science/labs/lab-06

| File | What it is |
|---|---|
| `list.c` | **Part A.** A linked list of numbers: insert at the head, print, search, free. |
| `queue.c` | **Part B.** A queue of names with a fixed capacity: enqueue, dequeue. |
| `dictionary.c`, `dictionary.h` | **Part C.** A hash table for a spell checker: load, check, size, unload. |
| `speller.c` | The spell checker that uses your dictionary. Do not edit. |
| `dictionaries/`, `texts/` | A small and a large word list, and texts to check. |
| `cs50.h`, `cs50.c`, `Makefile` | The CS50 library and `make list`, `make queue`, `make speller`. |
| `lab06.ipynb` | Playground notebook: how well do different hash functions spread words? Not graded. |
| `check.py`, `tests/` | The checks, one test file per part. Do not edit tests. |

```bash
make speller && ./speller dictionaries/small texts/cat.txt
valgrind ./speller dictionaries/small texts/cat.txt
python3 check.py
git add -A && git commit -m "Lab 6" && git push
```
