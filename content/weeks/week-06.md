---
week: 6
title: "Memory: Pointers, the Heap and Hexadecimal"
description: "The week that takes the hood off. Addresses, pointers, why a string was a char* all along, malloc and free, the stack and the heap, segmentation faults, and files and images as bytes."
module: m3
status: draft
lab: lab-05
reading: "K&R chapter 5.1–5.6; CS50 notes"
cs50:
  week: "4"
  title: "Memory"
  video: "https://youtu.be/db0H0U13YsA"
  notes: "https://cs50.harvard.edu/x/2026/notes/4/"
  slides: "https://cdn.cs50.net/2025/fall/lectures/4/lecture4.pdf"
  source: "https://cdn.cs50.net/2025/fall/lectures/4/src4.zip"
  pset: "https://cs50.harvard.edu/x/2026/psets/4/"
prep:
  - "This is the hardest week of the course. Watch the lecture twice if needed; the second time, draw the memory diagrams on paper as Malan draws them."
  - "Open <a href=\"https://pythontutor.com/c.html\" target=\"_blank\" rel=\"noopener\">Python Tutor for C</a> and step through the lecture's <code>swap.c</code>."
objectives:
  - "Read and write hexadecimal, and convert between hex, binary and decimal."
  - "Explain what an address is, and use & (address of) and * (dereference) correctly."
  - "State that a string is a char*, and explain why string comparison needs strcmp and copying needs a loop or strcpy."
  - "Allocate memory with malloc, release it with free, and use valgrind to find leaks."
  - "Draw the stack and the heap, and explain why swap needs pointers and what a segmentation fault is."
  - "Read and write files with fopen, fread, fwrite and fclose, and describe an image as a header plus pixel bytes."
wow:
  title: "‘Enhance!’ is impossible: a photo is a finite grid of bytes, and there is nothing behind them."
  text: "Every crime show zooms into a reflection to read a license plate. A 3-megapixel image is 9 million bytes and that is all the information there is; zooming shows bigger squares. This week you open image files byte by byte and see that a photo is just a header saying 'width, height' followed by red, green, blue, red, green, blue. Once you see it, you can recover deleted photos from a memory card, which is exactly what CS50's recover.c does."
industry:
  - { "t": "Memory bugs are the security headlines", "d": "Microsoft and Google report that about 70% of their serious security vulnerabilities are memory-safety bugs: use-after-free, buffer overflows, dangling pointers. Everything you learn this week is what those bugs are made of." }
  - { "t": "malloc is a whole subsystem", "d": "Allocators like jemalloc and tcmalloc are engineering marvels that every server process depends on. Facebook and Google each maintain their own." }
  - { "t": "Hex is the language of the low level", "d": "Memory addresses, colors in CSS (#1a2b3c), MAC addresses, error codes (0xC0000005), file signatures (FF D8 for JPEG). Reading hex fluently is a mark of a real engineer." }
  - { "t": "Rust exists because of this week", "d": "Rust is C's ideas with a compiler that refuses to build programs with these bugs. It is now in the Linux kernel, Android and Windows. You cannot appreciate it until you have felt the pain." }
resources:
  - { "title": "CS50x 2026 · Week 4 notes", "url": "https://cs50.harvard.edu/x/2026/notes/4/" }
  - { "title": "Pointer Fun with Binky (video)", "url": "https://www.youtube.com/watch?v=5VnDaHBi8dM", "note": "Stanford's 3-minute claymation on pointers. Yes, really." }
  - { "title": "Python Tutor for C", "url": "https://pythontutor.com/c.html", "note": "Step through any C program and watch memory." }
  - { "title": "Valgrind quick start", "url": "https://valgrind.org/docs/manual/quick-start.html" }
tags: ["pointers", "hexadecimal", "address", "malloc", "free", "valgrind", "stack", "heap", "segmentation fault", "strcmp", "file I/O", "BMP"]
---

## Topics

1. **Hexadecimal**: base 16, `0x` prefix, two hex digits per byte, RGB as `#RRGGBB`.
2. **Addresses and pointers**: `&x`, `int *p = &x;`, `*p = 50;`. Pointers are just numbers that happen to be addresses.
3. **Strings, revealed**: `string` is `char *`; `s[i]` is `*(s + i)`; comparing with `==` compares addresses (wrong); `strcmp`, `strcpy`, and copying by hand.
4. **Dynamic memory**: `malloc`, `free`, `NULL` checks, memory leaks, `valgrind`.
5. **Stack vs heap**: local variables and function frames on the stack; `malloc` on the heap; why `swap(int a, int b)` cannot work and `swap(int *a, int *b)` can.
6. **Files**: `fopen`, `fread`, `fwrite`, `fclose`; JPEG signatures; BMP headers and pixels; `scanf` and why `get_string` exists.

Full notes are published before the lecture. The lab, [Lab 5: Pointers and Pixels](/labs/lab-05), covers swap, string copying, malloc/free with valgrind, and a grayscale filter on a BMP.
