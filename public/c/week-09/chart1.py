# A bar chart: each student's total, sorted, with the class mean as a line

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("scores.csv")
labs = ["lab2", "lab3", "lab4", "lab5", "lab6", "lab7"]
df["total"] = df[labs].sum(axis=1)
df = df.sort_values("total")

colors = ["tab:red" if t < 30 else "tab:blue" for t in df["total"]]   # a list comprehension picks the colors
plt.barh(df["name"], df["total"], color=colors)
plt.axvline(df["total"].mean(), linestyle="--", color="gray", label="class mean")
plt.xlabel("total of six labs (out of 60)")
plt.title("Who needs a conversation?")
plt.legend()
plt.tight_layout()
plt.show()
