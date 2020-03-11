import matplotlib.pyplot as plt

default_fig = plt.figure('Default')
plt.xlabel("xLabel")
plt.ylabel("yLabel")

larger_fig = plt.figure('Larger')
plt.xlabel("xLabel", size=18, fontproperties='monospace')
plt.ylabel("yLabel", fontsize=18, fontproperties='monospace')

plt.show()
