# A scatter plot: does the pointers lab predict the data-structures lab?

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("scores.csv")

plt.scatter(df["lab5"], df["lab6"], s=80, alpha=0.7)
for _, row in df.iterrows():                       # label every point with the student's name
    plt.annotate(row["name"], (row["lab5"], row["lab6"]), xytext=(5, 5), textcoords="offset points", fontsize=8)
plt.xlabel("Lab 5 · pointers")
plt.ylabel("Lab 6 · hash table")
plt.title(f"Correlation: {df['lab5'].corr(df['lab6']):.2f}")
plt.show()
