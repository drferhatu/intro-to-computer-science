# The same two numbers, drawn honestly and dishonestly. Only the y-axis differs.

import matplotlib.pyplot as plt

sections = ["Section A", "Section B"]
means = [8.6, 8.2]

fig, (left, right) = plt.subplots(1, 2, figsize=(9, 3.5))

left.bar(sections, means)
left.set_ylim(0, 10)
left.set_title("Axis from 0: a small difference")

right.bar(sections, means)
right.set_ylim(8.1, 8.7)
right.set_title("Axis from 8.1: 'Section A crushes B'")

plt.tight_layout()
plt.show()
