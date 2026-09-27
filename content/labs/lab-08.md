---
lab: 8
week: 10
title: "Minimax and a Model"
description: "Write an unbeatable tic-tac-toe player with minimax, then call a large language model from Python with a system prompt you design and evaluate its answers."
assignment: lab08
status: draft
acceptUrl: ""
due: "2026-11-27 23:59"
duration: "90 min + finish at home"
points: 10
language: "Python"
files: ["tictactoe.py", "assistant.py", "eval.md"]
topics: ["minimax", "recursion", "APIs", "prompt engineering", "evaluation"]
---

## Plan

This lab opens in week 10. The full step-by-step page, the starter repository and the tests are published before that Monday; the plan below is final.

1. **tictactoe.py**: a `minimax(board, player)` that returns the best move; a game loop against the computer.
2. **assistant.py**: send a system prompt plus a user question to an LLM API (a key is provided for the lab) and print the answer.
3. **eval.md**: ten questions about week 6 (memory) asked to your assistant; mark each answer correct, partly correct or hallucinated.
4. **Explore notebook**: a decision tree learned from a tiny dataset, and a look at tokens.

## How it works

Same loop as every lab: accept on Classroom 50, open in Codespaces, solve the TODOs, `python3 check.py` until green, `git push`. See [how labs work](/labs) and the [setup guide](/guides/lab-setup).
