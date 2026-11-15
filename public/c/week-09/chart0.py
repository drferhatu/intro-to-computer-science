# A line chart: the class average of each lab
# pip install matplotlib

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("scores.csv")
labs = ["lab2", "lab3", "lab4", "lab5", "lab6", "lab7"]
means = df[labs].mean()

plt.plot(labs, means, marker="o")
plt.title("Class average by lab")
plt.xlabel("lab")
plt.ylabel("mean score (out of 10)")
plt.ylim(0, 10)                 # start the axis at zero: see chart3.py for why
plt.grid(alpha=0.3)
plt.savefig("average.png", dpi=150)   # write a file (for a report or a README)
plt.show()                            # and open a window (or draw under the cell in a notebook)
