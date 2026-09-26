---
lab: 11
week: 13
title: "Hash, Crack, Defend"
description: "Hash passwords, crack the weak ones with a dictionary attack, add salt so the attack stops working, and check a password against known breaches without ever sending it."
assignment: lab11
status: draft
acceptUrl: ""
due: "2026-12-20 23:59"
duration: "90 min + finish at home"
points: 10
language: "Python"
files: ["hashes.py", "crack.py", "salted.py", "pwned.py"]
topics: ["hashing", "salting", "dictionary attack", "k-anonymity", "APIs"]
---

## Plan

This lab opens in week 13. The full step-by-step page, the starter repository and the tests are published before that Monday; the plan below is final.

1. **hashes.py**: SHA-256 of a list of passwords, written to a file like a leaked database.
2. **crack.py**: recover every password that appears in a 10 000-word list by hashing candidates and comparing.
3. **salted.py**: add a random salt per user and show that the same attack now needs 10 000× more work.
4. **pwned.py**: send only the first five characters of a SHA-1 hash to the Have I Been Pwned range API and report how often the password has leaked.
5. **Explore notebook**: how long brute force takes at 10⁹ guesses per second for passwords of length 6–14.

## How it works

Same loop as every lab: accept on Classroom 50, open in Codespaces, solve the TODOs, `python3 check.py` until green, `git push`. See [how labs work](/labs) and the [setup guide](/guides/lab-setup).
