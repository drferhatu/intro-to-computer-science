#!/usr/bin/env bash
# Installs the test runner and the notebook kernel in the codespace (gcc, for the C cells of the notebook, is already there). Safe to run again.
set -e
pip install -q -r requirements.txt ipykernel matplotlib numpy
echo "✓ pytest, Jupyter, matplotlib and numpy are ready. Try:  python mario.py"
