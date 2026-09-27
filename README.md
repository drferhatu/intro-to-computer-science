# Introduction to Computer Science (YMT113) · Fall 2026

Course website for **Introduction to Computer Science**, Fırat University, Software Engineering (UOLP, taught in English).
Built on Harvard's CS50x 2026. Instructor: Assoc. Prof. Ferhat Uçar.

**Live site:** https://drferhatu.github.io/intro-to-computer-science/

## Structure

```
content/
  data/course.json         course info, meeting times, outcomes, grading, policies, books, tools, Classroom 50 and CS50 settings
  data/modules.json        six modules and their weeks
  data/schedule.json       Monday dates, exam week, final
  data/projects.json       semester project catalog (20 projects, 6 themes)
  weeks/week-NN.md(x)      one file per week (frontmatter: CS50 lecture to watch, prep, objectives, wow moment, industry, lab, notebook, resources)
  labs/lab-NN.md(x)        step-by-step lab instructions (students can start without the instructor)
  guides/                  setup guides (/guides/<name>)
  announcements/           announcements (kind: info | important | exam | lab | project)
labs/
  templates/labNN/         starter repository for each lab (published as a Classroom 50 template): C files, mini cs50 library, Makefile, tests, check.py, notebook, devcontainer
  autograders/labNN/       Classroom 50 declarative tests (tests.json)
notebooks/                 exploration notebooks that belong to weeks (rendered to public/notebooks/ at build time)
src/                       Astro pages, components (BitPlayground, Step, Terminal, NotebookEmbed …), design system (src/styles/global.css)
scripts/                   notebook builder, lab verifier, template publisher, content validator
public/slides/             lecture slides (PDF)
docs/                      maintainer notes (Turkish)
private/                   solutions and instructor-only notes; git-ignored, never published
```

## Develop

Node.js 22+, Python 3.12+ with `scripts/requirements-notebooks.txt`, gcc (for the C notebooks and lab tests).

```bash
npm install
npm run dev                                   # http://localhost:4321/intro-to-computer-science/
python scripts/build_notebooks.py --execute   # notebooks → public/notebooks/*.html
npm run build                                 # dist/ + search index
python scripts/validate_content.py            # content, schedule and link checks
python scripts/verify_lab.py lab01            # starter fails every test, solution passes
```

Every push to `main` builds and deploys to GitHub Pages (`.github/workflows/deploy.yml`).

## Labs

Labs are distributed and autograded with [Classroom 50](https://github.com/foundation50/classroom50/wiki)
and solved in GitHub Codespaces (VS Code in the browser with gcc, make, valgrind and the tests preinstalled).
Each lab also ships an exploration notebook that compiles and runs C inside Jupyter/Colab.
See `docs/OGRETIM-UYESI-REHBERI.md` for the instructor setup and the weekly routine.
