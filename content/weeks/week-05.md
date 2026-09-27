---
week: 5
title: "Algorithms: Searching, Sorting and Big O"
description: "Linear and binary search, three ways to sort, and a language for comparing them: Big O, Ω and Θ. Plus structs, and recursion, which is a function that calls itself."
module: m3
status: draft
lab: lab-04
reading: "K&R chapter 6.1–6.3 (structs); CS50 notes"
cs50:
  week: "3"
  title: "Algorithms"
  video: "https://youtu.be/6Svu_ae5ebk"
  notes: "https://cs50.harvard.edu/x/2026/notes/3/"
  slides: "https://cdn.cs50.net/2025/fall/lectures/3/lecture3.pdf"
  source: "https://cdn.cs50.net/2025/fall/lectures/3/src3.zip"
  pset: "https://cs50.harvard.edu/x/2026/psets/3/"
prep:
  - "Watch the lecture and pause at the sorting demos: predict the next step before Malan does it."
  - "Your personal project is announced today. Set up the project repository this week and make your first commit (a README with a plan)."
objectives:
  - "Implement linear search and binary search on arrays, and state their preconditions."
  - "Trace selection sort, bubble sort and merge sort by hand on eight numbers."
  - "Use Big O to classify algorithms as O(1), O(log n), O(n), O(n log n) or O(n²), and explain Ω and Θ."
  - "Define a struct to bundle related data, and use arrays of structs."
  - "Write a recursive function with a base case, and explain why merge sort is O(n log n)."
wow:
  title: "Sorting a million numbers: 12 days with bubble sort, 0.02 seconds with merge sort, on the same laptop."
  text: "n² for a million is a trillion steps; n log n is twenty million. The hardware did not change, the idea did. This is why 'just buy a faster server' rarely works and why algorithms is the interview question at every major software company. Today you learn to see the difference before you run the code."
industry:
  - { "t": "Every database index is binary search", "d": "A B-tree in PostgreSQL or MySQL finds one row among a billion in a few dozen steps, because the data is kept sorted. Without it, every query is a full scan." }
  - { "t": "Sorting is everywhere", "d": "Your feed, your search results, your bank statement, the leaderboard. Real systems use hybrids of merge sort and insertion sort (Timsort in Python and Java) chosen for exactly the reasons you learn this week." }
  - { "t": "Big O is the vocabulary of interviews", "d": "\"What is the complexity of your solution?\" is asked in nearly every technical interview. The answer is one of five letters you learn today." }
  - { "t": "Structs are records", "d": "A struct in C is a row in a database, a JSON object on the web, a class in Python. It is the first step from loose variables to organized data." }
resources:
  - { "title": "CS50x 2026 · Week 3 notes", "url": "https://cs50.harvard.edu/x/2026/notes/3/" }
  - { "title": "Sorting algorithm animations (Toptal)", "url": "https://www.toptal.com/developers/sorting-algorithms", "note": "Race the algorithms on different inputs." }
  - { "title": "Big-O Cheat Sheet", "url": "https://www.bigocheatsheet.com/", "note": "One page to keep." }
tags: ["linear search", "binary search", "selection sort", "bubble sort", "merge sort", "Big O", "recursion", "struct"]
---

## Topics

1. **Searching**: linear search on any array; binary search on a sorted array; pseudocode to C.
2. **Running time**: counting steps, best and worst case; **O** (upper bound), **Ω** (lower bound), **Θ** (both). The five common classes and where each algorithm lands.
3. **Structs**: `typedef struct { string name; string number; } person;` and arrays of structs, so searching a phone book means comparing `people[i].name`.
4. **Sorting**: selection sort, bubble sort (both O(n²)), and merge sort (O(n log n)) with a live demonstration.
5. **Recursion**: a function that calls itself, the base case, the call stack, and why merge sort is naturally recursive.

Full notes are published before the lecture. The lab, [Lab 4: Search and Sort](/labs/lab-04), implements searching, two sorts and a timing experiment.
