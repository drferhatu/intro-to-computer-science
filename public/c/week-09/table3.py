# New columns, groups, and saving the result

import pandas as pd

df = pd.read_csv("scores.csv")
labs = ["lab2", "lab3", "lab4", "lab5", "lab6", "lab7"]

df["total"] = df[labs].sum(axis=1)             # a new column: sum across each row
df["average"] = df[labs].mean(axis=1).round(2)
df["missing"] = (df[labs] == 0).sum(axis=1)    # how many labs scored zero

print(df[["name", "total", "average", "missing"]].sort_values("total", ascending=False))

print(df.groupby("section")[labs].mean().round(2))   # one row per section: the average of every lab

print(df[labs].mean().round(2))                # the average of each lab: which one was hardest?

df.to_csv("report.csv", index=False)           # write the enriched table back to a file
