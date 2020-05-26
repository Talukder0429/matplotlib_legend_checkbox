import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from checkboxLegend import checkboxLegend

fig1, ax1 = plt.subplots()

line1,  = plt.plot([1, 2], [1, 2], color='r', lw=2, label="R")
line2,  = plt.plot([1, 2], [2, 1], color='g', lw=4, label="G")
line3,  = plt.plot([1, 2], [3, 2], color='b', lw=8, label="B")
rect = mpatches.Rectangle((1, 4), 2, 2, label="rect")
ax1.add_patch(rect)
plt.legend()

fig2, ax2 = plt.subplots()

line1,  = plt.plot([1, 2], [1, 2], color='r', lw=2, label="R")
line2,  = plt.plot([1, 2], [2, 1], color='g', lw=4, label="G")
line3,  = plt.plot([1, 2], [3, 2], color='b', lw=8, label="B")
rect = mpatches.Rectangle((1, 4), 2, 2, label="rect")
ax2.add_patch(rect)
checkboxLegend(plt)

plt.show()