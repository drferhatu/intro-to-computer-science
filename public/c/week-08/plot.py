# Draw a chart in four lines (matplotlib, installed in Colab)

import matplotlib.pyplot as plt

weeks = [2, 3, 4, 5, 6, 7]
mean_score = [9.1, 9.83, 8.82, 9.11, 9.4, 9.2]

plt.plot(weeks, mean_score, marker="o")
plt.title("Average lab score by week")
plt.xlabel("week")
plt.ylabel("mean score / 10")
plt.show()
