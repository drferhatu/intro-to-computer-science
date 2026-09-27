---
week: 4
title: "Arrays, Strings and the Command Line"
description: "What the compiler really does in four steps, how to debug instead of guessing, and the first data structure: arrays, including strings, which are arrays of characters. Plus command-line arguments and a first taste of cryptography."
module: m2
status: draft
lab: lab-03
reading: "K&R chapters 1.6–1.9, 5.1–5.2 (skim)"
cs50:
  week: "2"
  title: "Arrays"
  video: "https://youtu.be/h5Gc1n8ZuU8"
  notes: "https://cs50.harvard.edu/x/2026/notes/2/"
  slides: "https://cdn.cs50.net/2025/fall/lectures/2/lecture2.pdf"
  source: "https://cdn.cs50.net/2025/fall/lectures/2/src2.zip"
  pset: "https://cs50.harvard.edu/x/2026/psets/2/"
prep:
  - "Watch the lecture with a terminal open and type <code>scores.c</code> and <code>string.c</code> yourself as they appear."
  - "Read the <a href=\"/project\">project catalog</a>: preferences are due <strong>next Monday, October 12</strong> by email."
objectives:
  - "Name the four stages of compilation (preprocessing, compiling, assembling, linking) and what make hides."
  - "Debug with printf, the VS Code debugger (debug50) and rubber-duck debugging."
  - "Declare, fill and loop over arrays, and pass arrays to functions."
  - "Explain that a string is a char array ending with '\\0', and use strlen, string indexing and ctype functions."
  - "Read command-line arguments through argc and argv, and return exit codes from main."
  - "Implement a Caesar cipher on strings."
wow:
  title: "A string is a lie: there is no such thing as text in C, only bytes and a zero at the end."
  text: "\"HI!\" is four bytes in memory: 72, 73, 33 and a 0 that marks the end. printf keeps printing until it meets that zero. Forget the zero and it prints whatever garbage comes next in memory, which is exactly how many real programs leaked passwords. The CS50 library's string type is just a nickname for 'the address of the first char', and by week 6 you will not need the nickname."
industry:
  - { "t": "Buffer overflows", "d": "Writing past the end of an array is the single most exploited bug class in history (Morris worm 1988, Heartbleed 2014). C lets you do it silently; that is why memory-safe languages like Rust exist, and why C programmers test bounds religiously." }
  - { "t": "argv is every CLI tool", "d": "git commit -m \"msg\", gcc -o hello hello.c, ls -l: every command-line program parses argv exactly as you do this week." }
  - { "t": "Cryptography is arithmetic on characters", "d": "Caesar is a toy, but the pattern, shift each byte by a key, is the ancestor of the stream ciphers that encrypt your Wi-Fi." }
  - { "t": "Exit codes drive automation", "d": "return 0 for success, non-zero for failure. Continuous-integration systems, including the autograder, read this number to decide whether your build is green." }
resources:
  - { "title": "CS50x 2026 · Week 2 notes", "url": "https://cs50.harvard.edu/x/2026/notes/2/" }
  - { "title": "C strings explained (Beej ch. 5 and 12)", "url": "https://beej.us/guide/bgc/html/split/Strings.html", "note": "Second explanation of the null terminator." }
  - { "title": "Compiler Explorer", "url": "https://godbolt.org/", "note": "See the assembling step for real." }
tags: ["arrays", "strings", "null terminator", "strlen", "ctype", "argc", "argv", "exit status", "Caesar cipher", "compilation", "debugging"]
---

## Topics

1. **Compilation, really**: preprocessing (`#include`), compiling to assembly, assembling to machine code, linking with libraries. `make` runs all four.
2. **Debugging**: `printf` probes, breakpoints and stepping in the debugger, and explaining your code to a rubber duck (or to cs50.ai).
3. **Arrays**: `int scores[3];`, zero-based indexing, loops over arrays, why an array's length must be passed to a function, and what happens when you read `scores[3]`.
4. **Strings**: `char` arrays terminated by `\0`; `strlen`; iterating characters; `toupper`, `isalpha` from `<ctype.h>`; ASCII arithmetic (`'a' + 1` is `'b'`).
5. **Command-line arguments**: `int main(int argc, string argv[])`, checking `argc`, and `return 1` for errors.
6. **Cryptography**: plaintext, key, ciphertext; the Caesar cipher as a loop over a string with `(c - 'A' + k) % 26`.

Full notes are published before the lecture. The lab, [Lab 3: Strings and Ciphers](/labs/lab-03), implements points 3–6.
