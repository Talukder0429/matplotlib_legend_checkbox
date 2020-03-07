import matplotlib as mpl
import matplotlib.pyplot as plt

initial_fig = plt.figure('initial')
plt.hlines(0.5, 0, 1) # will add a horizontal line with the initial color in the color cycle blue
plt.vlines(0.5, 0, 1, colors=None) # will add a vertical line with the initial default color black

white_fig = plt.figure('white')
with mpl.rc_context({'lines.color':'white'}): # sets the default line color to white
   plt.gca().set_facecolor('k') # sets background to black, for better visibility
   plt.hlines(0.5, 0, 1) # incorrectly uses the initial default, black
   plt.vlines(0.5, 0, 1, colors=None) # uses the new default white, as wanted.

plt.show()

# uncomment the following lines to save respective figures
# initial_fig.savefig('initial_fig.png')
# white_fig.savefig('white_fig.png')