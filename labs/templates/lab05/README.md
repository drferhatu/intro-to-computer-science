# Lab 5 · Pointers and Pixels

Introduction to Computer Science (YMT113) · Fall 2026 · Fırat University

## Student

<!-- Fill in both lines, then commit. -->
- Name:
- Student ID:

**Full instructions:** https://drferhatu.github.io/intro-to-computer-science/labs/lab-05

| File | What it is |
|---|---|
| `swap.c` | **Part A.** Make swap work with pointers. |
| `copy.c` | **Part B.** A real copy of a string with malloc, strcpy and free. |
| `leaks.c` | **Part C.** Three memory bugs to find with valgrind and fix. |
| `filter.c`, `bmp.h` | **Part D.** Grayscale and reflect filters for 24-bit BMP images. |
| `images/` | Small BMP files to try the filters on. |
| `cs50.h`, `cs50.c`, `Makefile` | The CS50 library and `make swap`, `make copy`, … |
| `lab05.ipynb` | Playground notebook: a BMP file byte by byte. Not graded. |
| `check.py`, `tests/` | The checks, one test file per part. Do not edit tests. |

```bash
make swap && ./swap            # compile and run one program
valgrind ./copy                # run under the memory referee
python3 check.py               # run all checks, as often as you like
git add -A && git commit -m "Lab 5" && git push    # submit (every push is graded)
```
