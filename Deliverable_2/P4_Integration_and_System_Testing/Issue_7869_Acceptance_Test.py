import matplotlib.pyplot as plt
import matplotlib as mpl
plt.style.use('dark_background')

# test legend doesn't show errors with no text
plt.figure("No Text")
plt.plot([0, 1], label="foo") # Have the label in the legend be “foo”
plt.legend() # Create the legend

# test legend doesn't overlap with one text
plt.figure("One Text")
plt.plot([0, 1], label="foo") # Have the label in the legend be “foo”
plt.text(0, 1, "Sample text here")  # Create a text object with the specified text
plt.legend() # Create the legend

# test legend doesn't overlap with two texts
plt.figure("Two Texts")
plt.plot([0, 1], label="foo") # Have the label in the legend be “foo”
plt.text(0.8, 0, "Sample Text here")  # Create a text object with the specified text
plt.text(0, 1, "Another Text")  # Create a text object with the specified text
plt.legend() # Create the legend

plt.show() #Show the graph
