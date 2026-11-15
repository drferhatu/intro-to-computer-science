# The same file with pandas: one line to load, one line to look, one line to summarize
# pip install pandas   (already there in Colab)

import pandas as pd

df = pd.read_csv("scores.csv")     # df is a DataFrame: a table with named columns

print(df.head())                   # the first five rows
print(df.shape)                    # (rows, columns)
print(df["lab7"].mean())           # one column, one number
print(df.describe())               # count, mean, min, max ... for every numeric column
