# From the field: a CSV of lab scores → an average per student, in 12 lines
# Run with a file like:
#   name,lab1,lab2,lab3
#   Mario,10,9,8
#   Luigi,7,10,9

import csv
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python grades.py scores.csv")

with open(sys.argv[1]) as file:
    for row in csv.DictReader(file):                      # each row is a dict: {"name": "Mario", "lab1": "10", ...}
        points = [int(v) for k, v in row.items() if k != "name"]
        average = sum(points) / len(points)
        print(f"{row['name']:10} {average:5.2f}")
