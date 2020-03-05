import matplotlib.pyplot as plt

plt.plot([0, 1, 2, 3])

# this will not set size correctly
plt.xlabel("xLabel", size=18, fontproperties='Sans')
plt.ylabel("yLabel", fontsize=18, fontproperties='Sans')

plt.show()
