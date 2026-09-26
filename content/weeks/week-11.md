---
week: 11
title: "SQL: The Language of Data"
description: "Flat files and their limits, relational databases, and SQL: creating tables, inserting, selecting, joining, indexing. Plus the two bugs every backend engineer must know: race conditions and SQL injection."
module: m4
status: draft
lab: lab-09
reading: "CS50 notes; SQLite tutorial"
cs50:
  week: "7"
  title: "SQL"
  video: "https://youtu.be/oqRU2So6Z2Y"
  notes: "https://cs50.harvard.edu/x/2026/notes/7/"
  slides: "https://cdn.cs50.net/2025/fall/lectures/7/lecture7.pdf"
  source: "https://cdn.cs50.net/2025/fall/lectures/7/src7.zip"
  pset: "https://cs50.harvard.edu/x/2026/psets/7/"
prep:
  - "Watch the lecture with the favorites.db example open in <code>sqlite3</code> in your codespace; type each query as it appears."
  - "Project prototype check-in is today in the lab: tag your repository <code>m3-prototype</code> before 15:00."
objectives:
  - "Read and write CSV files from Python and explain why flat files do not scale."
  - "Design a table with types, primary keys and foreign keys, and normalize a many-to-many relationship."
  - "Write SELECT queries with WHERE, ORDER BY, GROUP BY, LIMIT and JOIN."
  - "Explain what an index is and why it makes queries fast (week 5 and 7, again)."
  - "Describe race conditions and transactions."
  - "Explain SQL injection and prevent it with parameterized queries."
wow:
  title: "‘Robert’); DROP TABLE Students;--’ is a real attack, and one line of code stops it."
  text: "SQL injection is when user input is pasted into a query as text, so an attacker's input becomes part of the command. It has drained bank databases, leaked millions of passwords and topped the OWASP list for twenty years. The fix is to pass the input as a parameter, never as a string. Today you see the attack work on a toy database, and then you make it fail."
industry:
  - { "t": "SQL is the most used language after English", "d": "Every backend developer, data analyst, product manager and scientist writes SQL. It is the one language in this course you are guaranteed to use in any job." }
  - { "t": "SQLite is in your pocket", "d": "The database we use is inside every iPhone and Android phone, every browser and most apps: the most deployed software on Earth, and it is written in C." }
  - { "t": "Indexes are why apps feel fast", "d": "A B-tree index turns a full-table scan into binary search. The first thing a senior engineer checks on a slow query is the index." }
  - { "t": "Race conditions cost real money", "d": "Two requests decrementing the same stock count at once sold the same concert seat twice. Transactions and locks are how banks and ticket systems stay sane." }
resources:
  - { "title": "CS50x 2026 · Week 7 notes", "url": "https://cs50.harvard.edu/x/2026/notes/7/" }
  - { "title": "SQLite tutorial", "url": "https://www.sqlitetutorial.net/" }
  - { "title": "SQLBolt: interactive SQL lessons", "url": "https://sqlbolt.com/", "note": "Practice in the browser." }
  - { "title": "OWASP: SQL injection", "url": "https://owasp.org/www-community/attacks/SQL_Injection" }
tags: ["SQL", "SQLite", "database", "table", "primary key", "foreign key", "JOIN", "index", "transaction", "race condition", "SQL injection"]
---

## Topics

1. **Flat files**: CSV with Python's `csv` module, counting with a dict, and where it breaks (duplication, inconsistency, speed).
2. **Relational databases**: tables, rows, columns, types (INTEGER, REAL, TEXT, BLOB), `CREATE TABLE`, primary and foreign keys.
3. **CRUD**: `INSERT`, `SELECT`, `UPDATE`, `DELETE`; `WHERE`, `LIKE`, `ORDER BY`, `GROUP BY`, `LIMIT`, aggregate functions.
4. **Relationships**: one-to-many and many-to-many, join tables, `JOIN`.
5. **Indexes**: `CREATE INDEX`, B-trees, the timing difference on a large table.
6. **Python + SQL**: the `cs50` and `sqlite3` libraries, parameterized queries.
7. **Two classic bugs**: race conditions and transactions; SQL injection and its prevention.

Full notes are published before the lecture. The lab, [Lab 9: Query the World](/labs/lab-09), designs a schema, loads a CSV, answers questions with joins, and demonstrates and fixes an injection.
