import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox, TransformedBbox
from matplotlib.image import BboxImage
from pathlib import Path


c = Path.cwd() / "checked.png"
uc = Path.cwd() / "unchecked.png"


def set_onclick(bbox, state):
    def onclick(event):
        global state
        if event.button == 1 and bbox.contains(event)[0]:
            #print(state)
            if state:
                state=0
                bbox.set_data(plt.imread(uc))
            else:
                state=1
                bbox.set_data(plt.imread(c))
            plt.gcf().canvas.draw()
    plt.gcf().canvas.mpl_connect('button_press_event', onclick)

# Create figure and axes
fig,ax = plt.subplots()



state=1
# Add the Bbox Image to add the checked.png image
bb = Bbox.from_bounds(0.2, 0.2, 0.6, 0.6)
image_data = plt.imread(c,0)
tbb = TransformedBbox(bb, ax.transData)
bbox_image = BboxImage(tbb)
bbox_image.set_data(image_data)

set_onclick(bbox_image, state)
ax.add_artist(bbox_image)

plt.show()


