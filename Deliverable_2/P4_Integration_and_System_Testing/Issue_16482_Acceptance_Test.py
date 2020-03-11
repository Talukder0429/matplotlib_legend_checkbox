import matplotlib as mpl
import matplotlib.pyplot as plt

initial_fig = plt.figure('initial')
plt.hlines(0.5, 0, 1)
plt.vlines(0.5, 0, 1, colors=None)

white_fig = plt.figure('white')
with mpl.rc_context({'lines.color':'white'}): # sets the default line color to white
   plt.gca().set_facecolor('k')
   plt.hlines(0.5, 0, 1)
   plt.vlines(0.5, 0, 1, colors=None)

plt.show()