---
week: 7
title: "Data Structures: Linked Lists, Hash Tables and Trees"
description: "Now that you can allocate memory, you can build your own structures: linked lists that grow, hash tables that find things in constant time, binary search trees, tries, stacks and queues. And the trade-offs between them."
module: m3
status: draft
lab: lab-06
reading: "K&R chapter 6.5–6.6; CS50 notes"
cs50:
  week: "5"
  title: "Data Structures"
  video: "https://youtu.be/PmAI76OGE_E"
  notes: "https://cs50.harvard.edu/x/2026/notes/5/"
  slides: "https://cdn.cs50.net/2025/fall/lectures/5/lecture5.pdf"
  source: "https://cdn.cs50.net/2025/fall/lectures/5/src5.zip"
  pset: "https://cs50.harvard.edu/x/2026/psets/5/"
prep:
  - "Watch the lecture with paper: draw every linked-list operation as boxes and arrows."
  - "Midterm is next week. Start your review sheet: one page per week, weeks 2–7."
objectives:
  - "Explain why arrays are fast to index but slow to grow, and how a linked list trades one for the other."
  - "Implement a singly linked list in C: node struct, insert at head, search, free."
  - "Describe stacks (LIFO) and queues (FIFO) and where each is used."
  - "Explain hash tables: hash function, buckets, collisions, chaining, and why lookup is O(1) on average."
  - "Describe binary search trees and tries, and their running times."
  - "Choose a data structure for a problem by reasoning about its operations."
wow:
  title: "A hash table finds one word among 140 000 in the time it takes an array to check three."
  text: "CS50's speller loads a dictionary of 143 091 words. With linear search, checking one word costs up to 143 091 comparisons; with a hash table, about one. A ten-page essay is checked in milliseconds. The trick is a function that turns a word into a bucket number, and it is the same trick behind Python dictionaries, JavaScript objects, database indexes and the cache in your CPU."
industry:
  - { "t": "Everything is a hash table", "d": "Python dicts, Java HashMaps, Redis, Memcached, DNS caches, Git's object store (keyed by SHA-1). Learning to build one is learning how most of the software world stores things." }
  - { "t": "Linked lists in the kernel", "d": "The Linux scheduler, network buffers and file systems use linked lists and trees, written in exactly the C you write this week." }
  - { "t": "Tries power autocomplete", "d": "Your keyboard's suggestions, search-as-you-type and IP routing tables are tries: each keystroke walks one level down." }
  - { "t": "Stacks and queues are architecture", "d": "The call stack you met in week 5, undo history, browser back buttons: stacks. Print jobs, message queues like Kafka and RabbitMQ, event loops: queues." }
resources:
  - { "title": "CS50x 2026 · Week 5 notes", "url": "https://cs50.harvard.edu/x/2026/notes/5/" }
  - { "title": "VisuAlgo", "url": "https://visualgo.net/en", "note": "Animated linked lists, hash tables, BSTs and tries." }
  - { "title": "Data Structures: Trade-offs and Performance (instructor slides, 2025)", "url": "https://ferhatucar.notion.site/intro2compsci", "note": "In the previous course site's lecture 9." }
tags: ["linked list", "hash table", "hash function", "collision", "stack", "queue", "binary search tree", "trie", "abstract data type"]
---

## Topics

1. **Abstract data types**: what operations a structure supports, separate from how it is built. Stacks and queues as the simplest examples.
2. **Arrays revisited**: contiguous memory, O(1) indexing, O(n) insertion, `realloc`.
3. **Linked lists**: `typedef struct node { int number; struct node *next; } node;`, insert at head in O(1), search in O(n), the classic pointer-ordering bug, freeing a list.
4. **Trees**: binary search trees, O(log n) when balanced, recursion again.
5. **Hash tables**: array of linked lists, the hash function, collisions and load factor, why O(1) on average and O(n) in the worst case.
6. **Tries**: a tree keyed by characters, O(k) lookup for a k-letter word, memory cost.
7. **Trade-offs**: a table of time and space for each, and the questions to ask before choosing.

Full notes are published before the lecture. The lab, [Lab 6: Build a Hash Table](/labs/lab-06), builds a linked list and then a hash table for a word list, with valgrind-clean memory.
