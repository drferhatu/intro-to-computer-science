---
week: 10
title: "Artificial Intelligence: How It Actually Works"
description: "From decision trees and minimax to machine learning, neural networks and large language models. What a transformer does with your prompt, why models hallucinate, and how to use AI well as a programmer."
module: m4
status: draft
lab: lab-08
reading: "CS50 AI lecture notes"
cs50:
  week: "ai"
  title: "Artificial Intelligence"
  video: "https://youtu.be/-9bo8HlSxwQ"
  notes: "https://cs50.harvard.edu/x/2026/notes/ai/"
  slides: "https://cdn.cs50.net/2025/fall/lectures/ai/ai.pdf"
prep:
  - "Watch the lecture. Then ask an AI assistant (ChatGPT, Claude, Gemini or cs50.ai) to explain minimax to you, and note one thing it got wrong or vague."
  - "Bring a question you would like an LLM to answer about your project; we will test it in the lab."
objectives:
  - "Explain decision trees and the minimax algorithm, and play out tic-tac-toe with it."
  - "Describe machine learning as learning a function from examples, and reinforcement learning as learning from reward."
  - "Explain what a neural network is (weighted sums and nonlinearities) and what training does."
  - "Describe what a large language model predicts, what a transformer's attention does, and why hallucinations happen."
  - "Write system and user prompts that get reliably better results, and evaluate an answer critically."
  - "Call an LLM from a Python program through an API."
wow:
  title: "A language model has never seen a word. It sees numbers, and it predicts the next number."
  text: "Your prompt is cut into tokens, each token becomes a list of a few thousand numbers, and the model computes which number is most likely next, over and over. There is no lookup, no database of facts, no understanding in the way you mean it. That is why it can write a beautiful essay and also invent a court case that never existed. Knowing this makes you the person in the room who uses AI well."
industry:
  - { "t": "Every developer now works with an AI", "d": "GitHub reports most new code on the platform is written with Copilot assistance. The skill is not typing less; it is specifying clearly, reading critically and testing everything." }
  - { "t": "Minimax runs the games you play", "d": "Chess engines, game AI and many planning systems are minimax with pruning and heuristics. Stockfish evaluates tens of millions of positions per second with exactly this idea." }
  - { "t": "Recommendation systems are machine learning", "d": "Netflix, Spotify, TikTok and your ad feed are functions learned from your clicks. Understanding the loop, data → model → prediction → more data, is understanding modern media." }
  - { "t": "Hallucination is a product risk", "d": "Air Canada was ordered to honor a refund policy its chatbot invented. Companies now hire engineers whose job is evaluation: measuring how often the model is wrong." }
resources:
  - { "title": "CS50x 2026 · AI lecture notes", "url": "https://cs50.harvard.edu/x/2026/notes/ai/" }
  - { "title": "But what is a neural network? (3Blue1Brown)", "url": "https://www.youtube.com/watch?v=aircAruvnKk", "note": "The best 19 minutes on the topic." }
  - { "title": "Transformers, explained visually (3Blue1Brown)", "url": "https://www.youtube.com/watch?v=wjZofJX0v4M" }
  - { "title": "Claude API documentation", "url": "https://docs.claude.com/", "note": "For the lab's API call." }
tags: ["artificial intelligence", "minimax", "decision tree", "machine learning", "reinforcement learning", "neural network", "large language model", "transformer", "prompt engineering", "hallucination"]
---

## Topics

1. **Prompts**: system prompt versus user prompt; what cs50.ai's duck is instructed to do and not do.
2. **Decision trees and minimax**: tic-tac-toe as a game tree, scores of −1/0/+1, why it is exhaustive for small games and why chess needs pruning and heuristics.
3. **Machine learning**: learning a function from labeled examples; reinforcement learning, explore versus exploit, the Nim demo.
4. **Neural networks**: neurons as weighted sums, activation, layers, training as adjusting weights to reduce error; deep learning.
5. **Large language models**: tokens, embeddings, attention, next-token prediction, temperature, context windows, hallucination.
6. **Using AI as a programmer**: what to ask, what to verify, how to keep your own understanding, and course policy.

Full notes are published before the lecture. The lab, [Lab 8: Minimax and a Model](/labs/lab-08), implements minimax for tic-tac-toe in Python and calls an LLM API with a system prompt you design.
