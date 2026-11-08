# From the field: count answers in a survey file with Counter (a dict that counts for you)

from collections import Counter
import csv

# answers.csv has one column, "language", with one answer per student
with open("answers.csv") as file:
    answers = [row["language"] for row in csv.DictReader(file)]

counts = Counter(answers)
for language, n in counts.most_common():
    print(f"{language:12} {'#' * n}  {n}")
