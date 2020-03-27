import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.patches as patches


def add_checkbox(legend):
        # Get the handles and labels in the legend
        handles, labels = ax.get_legend_handles_labels()

        x = len(handles)
        y = len(labels)
        # Go through a loop to add a rectangle patch to each handle
        # and have the label be an empty string
        while (x>0 and y>0):
                handles.append(rect)
                labels.append('')
                x = x - 1
                y = y - 1
        # Create the legend with the added column so the rectangle patch can be
        # added to each row in the legend
        ax.legend(handles, labels, ncol=2)


# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 2, 3], 'k--', label='A')
ax.plot([1, 2, 3], [3, 2, 1], 'k:', label='B')
ax.plot([1, 3,5], [1, 2, 3], 'k', label='C')

legend = ax.legend()

# Create a Rectangle patch
rect = patches.Rectangle((0,0),2,2,linewidth=1,edgecolor='r',facecolor='none')

#Add the checkox to the legend
add_checkbox(legend)


plt.show()
