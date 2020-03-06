import numpy as np
import matplotlib.pyplot as plt

# Create 4 subplots
fig, axg = plt.subplots(2, 2, sharex=True, sharey=False,
                        figsize=(12, 8))

x = 100000 * np.arange(1000)
y = x/100000

num_plots = 3

# Show the xticks on the top right subplot
axg.flat[1].xaxis.set_tick_params(labelbottom=True)
for i in range(num_plots):
  axg.flat[i].plot(x, y, color=None)

plt.tight_layout()

# Make the bottom right subplot not visible
for aa in axg.flat[3:]:
  aa.set_visible(False)

plt.show()