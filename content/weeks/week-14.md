---
week: 14
title: "Human–Computer Interaction and How Software Gets Built"
description: "Software is used by people and built by teams. Usability principles you can apply to your project this week, and a tour of how industry ships software: Git branches, code review, tests, CI, and the roles on a team. The lab is a project workshop."
module: m6
status: draft
reading: "Stanford CS101: software; Nielsen's 10 usability heuristics"
cs50:
  week: "9"
  title: "Flask (optional: if your project has a web part)"
  notes: "https://cs50.harvard.edu/x/2026/notes/9/"
prep:
  - "Read <a href=\"https://www.nngroup.com/articles/ten-usability-heuristics/\" target=\"_blank\" rel=\"noopener\">Nielsen's 10 usability heuristics</a> and note two your project violates."
  - "Push everything: the workshop starts from your repository as it is at 15:00."
objectives:
  - "Apply usability heuristics (visibility of status, error prevention, consistency, feedback) to a command-line or web program."
  - "Explain affordances, feedback loops and why error messages should say what to do next."
  - "Describe the software development loop in industry: issue → branch → commits → pull request → review → tests → merge → deploy."
  - "Use Git branches and write a pull request description."
  - "Name the roles on a software team and what each does with your code."
  - "Prepare a five-minute technical demo."
wow:
  title: "The Therac-25 killed patients with a user interface, not a physics error."
  text: "A 1980s radiation-therapy machine delivered lethal overdoses because a fast typist could enter a mode the software did not expect, and the error message said only ‘MALFUNCTION 54’. The code was one person's, never reviewed, never tested against real use. Every practice in this week, usability, review, tests, exists because of stories like this. Your project's error messages matter."
industry:
  - { "t": "Pull requests are how code enters the world", "d": "At Google, Microsoft and every serious open-source project, no line of code is merged without a second person reading it. Code review is where most learning on the job happens." }
  - { "t": "CI is your autograder, grown up", "d": "The GitHub Actions run that grades your labs is the same system that runs a company's tests on every push. You have been using industry tooling since week 2." }
  - { "t": "UX is a profession", "d": "Designers, researchers and accessibility specialists work alongside engineers. The heuristics you learn today are their daily checklist." }
  - { "t": "Demos decide", "d": "Startups raise money, teams get budgets and features ship on the strength of a five-minute demo. Week 15 is practice for that." }
resources:
  - { "title": "10 Usability Heuristics (Nielsen Norman Group)", "url": "https://www.nngroup.com/articles/ten-usability-heuristics/" }
  - { "title": "Stanford CS101: Software", "url": "https://web.stanford.edu/class/cs101/software-1.html" }
  - { "title": "GitHub Flow", "url": "https://docs.github.com/en/get-started/using-github/github-flow" }
  - { "title": "The Missing Semester: version control", "url": "https://missing.csail.mit.edu/2020/version-control/" }
tags: ["HCI", "usability", "heuristics", "Git", "branches", "pull request", "code review", "CI", "demo"]
---

## Topics

1. **People first**: affordances, feedback, consistency, error prevention and recovery; good and bad error messages from your own labs.
2. **Nielsen's heuristics** applied to a command-line program and to a web page.
3. **How software is built**: issues, branches, commits, pull requests, review, automated tests, CI/CD, releases; the roles: developer, reviewer, QA, designer, product manager, SRE.
4. **Git beyond push**: `git branch`, `git checkout -b`, `git merge`, resolving a conflict, tagging `v1.0`.
5. **The demo**: structure (problem, 30 seconds; live demo, 3 minutes; what you learned, 1 minute; questions), rehearsal, and what to do when it crashes live.

## No new lab: project workshop

The lab slot is yours. Bring your project to the room and use the instructor: code review on request, help with tests and README, and a dry run of your demo in front of one other student.
