# Last week's way: the csv module and a loop. It works, and it is already 10 lines for one average.

import csv

with open("scores.csv") as file:
    rows = list(csv.DictReader(file))

total = 0
for row in rows:
    total += int(row["lab7"])

print(f"{len(rows)} students, Lab 7 average {total / len(rows):.2f}")
