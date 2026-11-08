# Strings in Python: no '\0', no strlen, no malloc, and dozens of methods

s = "Fırat University"

print(len(s))                 # length, instantly (Python stores it; no counting to '\0')
print(s[0], s[-1])            # first and last character
print(s[0:5])                 # a SLICE: characters 0,1,2,3,4 → "Fırat"
print(s[6:])                  # from 6 to the end
print(s.upper())              # FIRAT UNIVERSITY
print(s.lower())              # fırat university
print(s.replace("Fırat", "Firat"))
print(s.startswith("F"), s.endswith("y"))
print(s.split(" "))           # ['Fırat', 'University'] – a list!
print("-".join(["a", "b", "c"]))
print("   padded   ".strip())
print("abc" < "abd")          # strings compare alphabetically with <, ==, no strcmp
print("niversity" in s)       # substring test

# Strings are immutable: you make new ones, you never edit in place
t = s + " · Elazığ"
print(t)
