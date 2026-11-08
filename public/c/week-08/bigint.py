# No overflow in Python: integers grow as large as memory allows

# In C, an int stops at 2 147 483 647 and a long at about 9.2 × 10^18.
print(2 ** 31)          # 2147483648, already past a C int
print(2 ** 64)          # 18446744073709551616
print(2 ** 200)         # 200 bits, no problem
print(100 * 99 * 98 * 97 * 96 * 95 * 94 * 93 * 92 * 91)

# Floats are the SAME hardware as in C, so the imprecision from week 3 is still there
print(0.1 + 0.2)        # 0.30000000000000004
print(f"{1 / 3:.50f}")  # the same 1/3 you saw in C
