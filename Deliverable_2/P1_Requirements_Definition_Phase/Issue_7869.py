import matplotlib.pyplot as plt
import matplotlib as mpl
plt.style.use('dark_background')

plt.figure()
plt.plot([0, 1], label="foo") # Have the label in the legend be “foo”
plt.text(.05, .95, "Sample Text here")  # Create a text object with the specified text
plt.legend() # Create the legend

plt.show() #Show the graph
