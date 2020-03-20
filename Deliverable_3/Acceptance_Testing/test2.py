import numpy as np
from matplotlib import patches
import matplotlib.pyplot as plt
import matplotlib as mpl


fig, ax = plt.subplots()

# add a line
x1 = 0
x2 = 2
y1 = 2
line1 = ax.plot([x1,x2], [y1,y1], color='k', label='line1')

# add a bar graph
N = 3
data = (1, 2, 3)
width = .2
barg = ax.bar(np.arange(N), data, width, color='b', label="bar")

# add a circle
x = 1
y = 3
r = .5
circle = patches.Circle((x, y), r, color='r', label="circle")
ax.add_patch(circle)

# add the legend
leg = ax.legend(checkbox=True)

plt.show()