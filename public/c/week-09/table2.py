# Selecting: columns by name, rows by a condition

import pandas as pd

df = pd.read_csv("scores.csv")

print(df["name"])                              # one column (a Series)
print(df[["name", "lab6", "lab7"]])            # several columns (a smaller DataFrame)

print(df[df["lab6"] < 5])                      # rows where the condition is True
print(df[(df["section"] == "B") & (df["lab7"] == 10)])   # two conditions: & for and, | for or

print(df.sort_values("lab6", ascending=False).head(3))   # top three in Lab 6
