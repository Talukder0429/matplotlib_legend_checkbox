import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path

# getting path of test image, and importing
image_path = Path.cwd() / "gui_image_interaction.png"
img = mpimg.imread(image_path, 0)

# creating figure and axes, and showing the imported image
fig, ax = plt.subplots()
imgplot = ax.imshow(img)
plt.axis('off')

# the callback function, when the image is clicked, it will print to console


def onclick(event):
    if event.xdata != None and event.ydata != None:
        print("the image was clicked")
    else:
        print("you clicked outside the image")


# listening for when the image is clicked on
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
