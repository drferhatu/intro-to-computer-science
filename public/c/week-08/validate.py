# The input-validation loop, Python style: keep asking until int() succeeds and the value is in range

while True:
    try:
        height = int(input("Height: "))
    except ValueError:
        print("That is not a number.")
        continue
    if 1 <= height <= 8:
        break
    print("Between 1 and 8, please.")

for i in range(height):
    print(" " * (height - i - 1) + "#" * (i + 1))
