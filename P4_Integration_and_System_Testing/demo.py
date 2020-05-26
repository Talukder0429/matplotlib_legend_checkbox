import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from checkboxLegend import checkboxLegend

line1,  = plt.plot([1, 2], [1, 2], color='r', lw=2)
line2,  = plt.plot([1, 2], [2, 1], color='g', lw=4)
line3,  = plt.plot([1, 2], [3, 2], color='b', lw=8)
line2.set_visible(0)
rect = mpatches.Rectangle((1, 4), 2, 2)
rect.set_visible(0)
ax = plt.gca()
ax.add_patch(rect)
checkboxLegend(plt, [line1, line2, line3, rect], [
                  "R", "G", "B", "rect"], fontsize=16)
plt.show()
