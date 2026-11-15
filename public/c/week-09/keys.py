# Keeping a secret out of your code: read it from the environment, never type it into a file you commit
# pip install python-dotenv
#
# 1. Create a file named .env next to this program with one line:   API_KEY=abc123
# 2. Add .env to .gitignore, so Git never sees it.
# 3. Commit a file named .env.example with   API_KEY=   so the next person knows what to create.

import os
import sys

from dotenv import load_dotenv

load_dotenv()                          # reads .env, if there is one, into the environment
key = os.environ.get("API_KEY")        # None if it is not set

if not key:
    sys.exit("Set API_KEY in a .env file (see .env.example).")

print(f"Using a key that ends in ...{key[-3:]}")      # never print the whole key, even in a log
