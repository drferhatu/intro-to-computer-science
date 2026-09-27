#!/usr/bin/env bash
# Installs the C toolchain and the test runner in the codespace. Safe to run again.
set -e
sudo apt-get update -qq
sudo apt-get install -y -qq gcc make gdb valgrind > /dev/null
pip install -q -r requirements.txt ipykernel
echo "✓ gcc, make, gdb, valgrind and pytest are ready. Try:  make hello && ./hello"
