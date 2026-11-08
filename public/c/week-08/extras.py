# Five small Python tools that make everyday code shorter: enumerate, zip, tuples, sets, list comprehensions

names = ["Mario", "Luigi", "Peach"]
scores = [72, 85, 91]

# enumerate: index and value at once (no i = 0 ... i += 1)
for i, name in enumerate(names):
    print(i, name)

# zip: walk two lists together
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# a tuple is a fixed pair (or triple ...), and Python unpacks it for you
point = (3, 4)
x, y = point
print(x, y)

# a set keeps each value once and answers "is it in there?" instantly (it is a hash table)
seen = set()
for w in ["cat", "dog", "cat", "bird", "dog"]:
    seen.add(w)
print(seen, len(seen))

# a list comprehension: build a list in one line
squares = [n * n for n in range(10)]
passed = [s for s in scores if s >= 80]
print(squares)
print(passed)

# sorted with a key: sort names by their score
pairs = list(zip(names, scores))
print(sorted(pairs, key=lambda p: p[1], reverse=True))
