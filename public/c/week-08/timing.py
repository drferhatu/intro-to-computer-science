# How much slower is Python than C? Measure, do not guess.
# Adds the numbers 0 .. n-1 the slow way (a loop), then with the built-in sum, then with NumPy.

import time

n = 10_000_000

start = time.perf_counter()
total = 0
for i in range(n):
    total += i
print(f"for loop      {time.perf_counter() - start:6.3f} s   total = {total}")

start = time.perf_counter()
total = sum(range(n))
print(f"sum(range)    {time.perf_counter() - start:6.3f} s   total = {total}")

try:
    import numpy as np
    start = time.perf_counter()
    total = int(np.arange(n, dtype=np.int64).sum())
    print(f"numpy         {time.perf_counter() - start:6.3f} s   total = {total}")
except ImportError:
    print("numpy is not installed here (pip install numpy)")

# The same loop in C (timing.c) takes about 0.01 s. NumPy is C underneath: that is why it keeps up.
