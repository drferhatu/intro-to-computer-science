# Dynamic typing: a variable is a name tag, and the tag can move to a value of another type

x = 50          # an int
print(x, type(x))

x = "fifty"     # the same name, now a str: no declaration, no error
print(x, type(x))

x = 50.0        # and now a float
print(x, type(x))

# Python still has types; it just checks them when the line runs, not before
print(1 + 2)          # 3
print("1" + "2")      # 12  (two strings glued together)
print(int("1") + 2)   # 3   (convert first, then add)
