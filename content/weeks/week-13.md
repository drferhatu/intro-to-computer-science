---
week: 13
title: "The Internet, Hardware and Security"
description: "Behind the wires: how packets cross the planet, what a CPU and memory hierarchy really are, and cybersecurity for people who now write code: passwords, hashing, encryption, phishing and the attacks you learned to cause in weeks 4, 6 and 11."
module: m5
status: draft
lab: lab-11
reading: "Stanford CS101: hardware, networks; CS50 Cybersecurity lectures 0–1"
cs50:
  week: "cyber"
  title: "CS50 Cybersecurity (lectures 0–1: Securing Accounts, Securing Data)"
  notes: "https://cs50.harvard.edu/cybersecurity/"
prep:
  - "Read Stanford CS101's short chapters on <a href=\"https://web.stanford.edu/class/cs101/network-1-introduction.html\" target=\"_blank\" rel=\"noopener\">networks</a> and <a href=\"https://web.stanford.edu/class/cs101/hardware-1.html\" target=\"_blank\" rel=\"noopener\">hardware</a>."
  - "Watch CS50 Cybersecurity lecture 0 (Securing Accounts). Then turn on two-factor authentication on your GitHub account if you have not."
objectives:
  - "Trace a packet from your laptop to a server: Wi-Fi, router, ISP, backbone, DNS, TCP handshake, HTTP, TLS."
  - "Describe a CPU, RAM, storage and the memory hierarchy, and relate it to the stack and heap of week 6."
  - "Explain password hashing and salting, and why a leaked hash is still a problem."
  - "Explain symmetric and public-key encryption at the level of 'what is shared and what is secret', and what HTTPS protects."
  - "Recognize phishing, SQL injection, buffer overflows and weak defaults as the same failure: trusting input."
  - "Apply basic hygiene: password managers, 2FA, updates, least privilege."
wow:
  title: "Your Wi-Fi password never leaves your laptop, and the server can still verify you know it."
  text: "That sounds impossible, and it is the everyday magic of cryptography: hashing lets a server check a password it never stores, and public-key encryption lets two strangers agree on a secret while the whole Internet listens. Both come from mathematics you can read in an afternoon, and both are why online banking exists at all."
industry:
  - { "t": "Security is now everyone's job", "d": "The bugs in weeks 4 (buffer overflow), 6 (use-after-free) and 11 (SQL injection) are the top of every vulnerability list. Companies pay bounties in the hundreds of thousands of dollars for them." }
  - { "t": "The cloud is other people's computers", "d": "AWS, Azure and Google Cloud are data centers full of the same CPUs and RAM you learn about, rented by the second. Knowing the hardware is knowing what you pay for." }
  - { "t": "HTTPS everywhere", "d": "Since Let's Encrypt made certificates free (2015), the web went from mostly unencrypted to over 95% encrypted. The padlock is TLS, built on the public-key ideas of this week." }
  - { "t": "Phishing beats technology", "d": "Most breaches start with a person, not a bug. The 2FA you turn on today is the single most effective defense there is." }
resources:
  - { "title": "CS50's Introduction to Cybersecurity", "url": "https://cs50.harvard.edu/cybersecurity/", "note": "Free, non-technical, excellent." }
  - { "title": "Stanford CS101: The Internet", "url": "https://web.stanford.edu/class/cs101/network-3-internet.html" }
  - { "title": "How does HTTPS work? (illustrated)", "url": "https://howhttps.works/" }
  - { "title": "Have I Been Pwned", "url": "https://haveibeenpwned.com/", "note": "Check whether your email appears in a known breach." }
tags: ["Internet", "TCP/IP", "DNS", "HTTP", "HTTPS", "TLS", "CPU", "RAM", "hashing", "salting", "encryption", "public key", "phishing", "2FA"]
---

## Topics

1. **Hardware**: CPU, cores and clock speed, RAM versus SSD, the memory hierarchy (registers, cache, RAM, disk) and why the stack and heap of week 6 live in RAM.
2. **Networks**: packets, IP addresses, routers and the path across the Internet; DNS; TCP versus UDP; ports; a `traceroute` live.
3. **The web layer**: HTTP again, cookies and sessions, what a server and a CDN are.
4. **Securing accounts**: password entropy, brute force and dictionary attacks, hashing and salting, password managers, 2FA, passkeys.
5. **Securing data**: symmetric encryption, public-key encryption, digital signatures, HTTPS and certificates, end-to-end encryption.
6. **Attacks you can now explain**: phishing, SQL injection, buffer overflow, cross-site scripting, and the one rule behind all defenses: never trust input.

Full notes are published before the lecture. The lab, [Lab 11: Hash, Crack, Defend](/labs/lab-11), hashes passwords in Python, cracks weak ones, adds salt, and checks a password against the Have I Been Pwned API without sending it.
