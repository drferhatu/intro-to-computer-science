---
week: 12
title: "The Web: HTML, CSS and JavaScript"
description: "What happens when you type a URL, and how a page is built: HTML for structure, CSS for style, JavaScript for behavior. By the end of the lab you have a page that reacts to the user."
module: m5
status: draft
lab: lab-10
reading: "CS50 notes; MDN 'Getting started with the web'"
cs50:
  week: "8"
  title: "HTML, CSS, JavaScript"
  video: "https://youtu.be/yYst7puZXjw"
  notes: "https://cs50.harvard.edu/x/2026/notes/8/"
  slides: "https://cdn.cs50.net/2025/fall/lectures/8/lecture8.pdf"
  source: "https://cdn.cs50.net/2025/fall/lectures/8/src8.zip"
  pset: "https://cs50.harvard.edu/x/2026/psets/8/"
prep:
  - "Watch the lecture, then open this very page, press F12 and change something in the Elements tab. That is the lab's first step."
  - "Look at last year's <a href=\"https://github.com/drferhatu/Introt-to-Comp-Sci---html-css-js-\" target=\"_blank\" rel=\"noopener\">HTML/CSS/JS examples repository</a>: five interactive examples we build on."
objectives:
  - "Explain the request–response model: URL, DNS, HTTP GET and POST, status codes, and what a server is."
  - "Write valid HTML with headings, paragraphs, lists, links, images, forms and inputs."
  - "Style a page with CSS selectors, properties, the box model and flexbox, and explain the cascade."
  - "Write JavaScript that responds to events and changes the DOM."
  - "Use the browser's developer tools to inspect elements, network requests and console output."
  - "Recognize the same five ideas (variables, conditions, loops, functions, events) in a third language."
wow:
  title: "Every website you have ever used sent you its source code. You can read all of it."
  text: "Press F12 on any site: the HTML, the CSS, the JavaScript, every network request and every cookie is there, because the browser has to have it to show the page. The web is the only major platform where the client's code is open by design. That is why it is the best place to learn, and why security on the web can never rely on hiding things."
industry:
  - { "t": "The browser is the platform", "d": "Gmail, Figma, VS Code (the editor you use in Codespaces), Google Docs and Slack are web apps. The most widely used desktop application in the world, VS Code, is HTML, CSS and JavaScript." }
  - { "t": "JavaScript is the most used language", "d": "Every survey of developers puts JavaScript first. Node.js runs it on servers too, so one language covers the whole stack." }
  - { "t": "Accessibility is law", "d": "Semantic HTML (real headings, labels on inputs, alt text) is what screen readers use. In the EU and the US, inaccessible sites bring lawsuits and fines." }
  - { "t": "Frameworks are abstraction, again", "d": "React, Vue and Svelte are to JavaScript what your custom Scratch block was to ten blocks: once the raw thing works, you wrap it. This site is built with Astro and Tailwind, exactly such wrappers." }
resources:
  - { "title": "CS50x 2026 · Week 8 notes", "url": "https://cs50.harvard.edu/x/2026/notes/8/" }
  - { "title": "MDN Web Docs", "url": "https://developer.mozilla.org/en-US/docs/Learn", "note": "The reference for HTML, CSS and JavaScript." }
  - { "title": "Last year's HTML/CSS/JS examples", "url": "https://github.com/drferhatu/Introt-to-Comp-Sci---html-css-js-", "note": "Counter, to-do list, form validation, CSS showcase, gradient generator." }
  - { "title": "Flexbox Froggy", "url": "https://flexboxfroggy.com/", "note": "Learn flexbox as a game." }
tags: ["HTML", "CSS", "JavaScript", "DOM", "HTTP", "URL", "DNS", "flexbox", "events", "developer tools"]
---

## Topics

1. **The Internet in one paragraph**: IP addresses, DNS, routers, TCP/IP, HTTP; the request `GET / HTTP/1.1` and the response `200 OK`; status codes 301, 404, 500.
2. **HTML**: tags, attributes, the tree (DOM), `<head>` and `<body>`, headings, lists, links, images, video, forms and inputs, validation attributes.
3. **CSS**: selectors (type, class, id), properties, the box model, inheritance and the cascade, flexbox, responsive basics, external stylesheets, frameworks like Bootstrap and Tailwind.
4. **JavaScript**: `let`, functions, `document.querySelector`, `addEventListener`, changing text and style, forms without reload, a little `setInterval`.
5. **Developer tools**: Elements, Console, Network; reading a request; editing a live page.

Full notes are published before the lecture. The lab, [Lab 10: Your First Web Page](/labs/lab-10), builds a page with a form, styles it, and adds JavaScript that responds to the user, published on GitHub Pages.
