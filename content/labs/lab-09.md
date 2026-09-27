---
lab: 9
week: 11
title: "Query the World"
description: "Design tables for a real CSV, load it into SQLite, answer questions with SELECT and JOIN, add an index, and demonstrate and fix an SQL injection."
assignment: lab09
status: draft
acceptUrl: ""
due: "2026-12-04 23:59"
duration: "90 min + finish at home"
points: 10
language: "SQL + Python"
files: ["schema.sql", "queries.sql", "load.py", "injection.py"]
topics: ["SQL", "SQLite", "schema", "JOIN", "index", "parameterized queries"]
---

## Plan

This lab opens in week 11. The full step-by-step page, the starter repository and the tests are published before that Monday; the plan below is final.

1. **schema.sql**: tables with primary and foreign keys for a students/courses/enrollments dataset.
2. **load.py**: read the CSV and insert rows with parameterized queries.
3. **queries.sql**: eight questions, from a simple WHERE to a three-table JOIN with GROUP BY; time one before and after CREATE INDEX.
4. **injection.py**: a login check built with string formatting, an input that bypasses it, and the parameterized fix.
5. **Explore notebook**: pandas versus SQL on the same questions.

## How it works

Same loop as every lab: accept on Classroom 50, open in Codespaces, solve the TODOs, `python3 check.py` until green, `git push`. See [how labs work](/labs) and the [setup guide](/guides/lab-setup).
