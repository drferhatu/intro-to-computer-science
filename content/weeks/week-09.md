---
week: 9
title: "Python in Practice: Data, Charts, APIs and Your Project"
description: "Last week was the language; this week is the work. Read a spreadsheet with pandas, draw it with matplotlib, pull live data from a web API, organize a real project into files and an environment, and test it. The toolkit of the AI and data weeks ahead, and of your semester project."
module: m4
status: draft
lab: lab-07
reading: "CS50P notes on libraries and file I/O; pandas 10-minute tutorial"
cs50:
  week: "P"
  title: "No CS50x lecture this week: CS50P lectures 4 (Libraries) and 6 (File I/O) are the closest match"
  video: "https://cs50.harvard.edu/python/weeks/4/"
  notes: "https://cs50.harvard.edu/python/notes/4/"
  slides: ""
  source: ""
  pset: "https://cs50.harvard.edu/python/psets/4/"
prep:
  - "Finish Lab 7 (due Friday, November 13). This week's lecture builds on it."
  - "Have Python working locally with Miniconda and VS Code, as set up on the week 8 page, and bring your laptop. This is the first week where your own machine matters."
  - "The midterm is Wednesday, November 25, 12:00–13:00, rooms A304–A305, weeks 1–7 only: see the <a href=\"/guides/midterm\">midterm page</a>. Start the one-page-per-week sheet now."
objectives:
  - "Load a CSV into a pandas DataFrame, select columns and rows, compute summaries and group by a column."
  - "Draw line, bar and scatter charts with matplotlib and read them critically."
  - "Call a web API with requests, parse JSON, and handle errors and rate limits."
  - "Organize a program into modules and functions, keep secrets out of code, and write a first test with pytest."
  - "Set up a project folder: environment, requirements.txt, README, Git, and run it from a clean clone."
tags: ["pandas", "matplotlib", "requests", "JSON", "modules", "pytest", "virtual environment", "project"]
---

## Plan

1. **A spreadsheet in three lines**: `pd.read_csv`, `.head()`, `.describe()`; columns, filters, `groupby`; the lab scores of this course as the running example.
2. **Charts you can trust**: `plot`, `bar`, `scatter`, labels and titles; what a chart hides.
3. **Live data**: `requests.get`, status codes, `.json()`, a loop over pages; the GitHub API and a public weather API.
4. **From a script to a project**: functions in modules, `if __name__ == "__main__"`, `requirements.txt`, a `.env` file for keys, a `tests/` folder with one pytest test, `README.md`.
5. **Project clinic**: the lab slot is for your semester project. Milestone 3 (prototype) is due in week 11; bring your repository and leave with a running skeleton and a commit.

No new graded lab this week: finish [Lab 7](/labs/lab-07), work on your project in the lab slot, and review for the [midterm](/guides/midterm). Full notes are published before the lecture.
