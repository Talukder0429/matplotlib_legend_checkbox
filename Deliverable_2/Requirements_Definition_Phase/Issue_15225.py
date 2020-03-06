import numpy as np
import matplotlib.pyplot as plt

sub_w, sub_h = 6, 4
# Figure layout. Want to plot three subplots, but need to allocate a grid of 4.
fig, axg = plt.subplots(2, 2, sharex=True, sharey=False,
                        figsize=(sub_w * 2, sub_h * 2))
x = 100000 * np.arange(1000, dtype=np.float32)
y = np.sin(x / 10000000)

num_plots = 3
num_lines_per_plot = 2
# The following line makes sure xticks are shown on the top right subplot.
axg.flat[1].xaxis.set_tick_params(labelbottom=True)
for i in range(num_plots):
  ax = axg.flat[i]
  for j in range(num_lines_per_plot):
    ax.plot(x, y * (i + j + 1), color=None)

plt.tight_layout()
# Remove bottom left grid
for aa in axg.flat[3:]:
  aa.set_visible(False)

plt.show()