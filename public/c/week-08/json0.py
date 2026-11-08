# JSON: the dict-and-list format the whole web speaks. Python converts both ways in one call.

import json

student = {"name": "Mario", "id": 220541001, "labs": [10, 9, 8], "project": None}

text = json.dumps(student, indent=2)     # dict → text (what an API sends)
print(text)

back = json.loads(text)                  # text → dict (what you get from an API)
print(back["labs"][0], back["project"])
