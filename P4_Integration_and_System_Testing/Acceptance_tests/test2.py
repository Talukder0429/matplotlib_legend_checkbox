import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from checkboxLegend import checkboxLegend

fig1, ax1 = plt.subplots()

line1,  = plt.plot([1, 2], [1, 2], color='r', lw=2)
line2,  = plt.plot([1, 2], [2, 1], color='g', lw=4)
line3,  = plt.plot([1, 2], [3, 2], color='b', lw=8)
rect = mpatches.Rectangle((1, 4), 2, 2)
ax1.add_patch(rect)
plt.legend(["R", "G", "B", "rect"])

fig2, ax2 = plt.subplots()

line1,  = plt.plot([1, 2], [1, 2], color='r', lw=2)
line2,  = plt.plot([1, 2], [2, 1], color='g', lw=4)
line3,  = plt.plot([1, 2], [3, 2], color='b', lw=8)
rect = mpatches.Rectangle((1, 4), 2, 2)
ax2.add_patch(rect)
checkboxLegend(plt, ["R", "G", "B", "rect"])

plt.show()