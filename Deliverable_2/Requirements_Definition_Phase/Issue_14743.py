import matplotlib.pyplot as plt
import numpy as np
f, ax = plt.subplots() # create a single figure fig with an array of axes ax
N = 50 # Number of samples to generate
ax.set_yscale('logit') # apply logit scale to y axis
ax.set_ylim((0.1,0.9)) # this is the step where we set a limit on the y axis
# plot evenly spaced numbers over a specified interval
ax.plot(np.linspace(0,1,N), np.linspace(0.1,0.9,N))
plt.show() # generate the plot for user to view
