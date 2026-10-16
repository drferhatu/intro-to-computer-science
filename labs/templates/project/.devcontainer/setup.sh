#!/usr/bin/env bash
# gcc, make, gdb, valgrind for C projects; Python 3 and pytest are already in the image.
set -e
sudo apt-get update -qq
sudo apt-get install -y -qq gcc make gdb valgrind > /dev/null
pip install -q pytest
echo "✓ ready. Try:  make && ./program"
