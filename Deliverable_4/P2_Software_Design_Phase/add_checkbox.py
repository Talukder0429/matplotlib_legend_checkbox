import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox, TransformedBbox
from matplotlib.image import BboxImage
from pathlib import Path


c = Path.cwd() / "checked.png"

# Create figure and axes
fig, ax = plt.subplots()


# Add the Bbox Image to add the checked.png image
bb = Bbox.from_bounds(0.2, 0.2, 0.6, 0.6)
image_data = plt.imread(c, 0)
tbb = TransformedBbox(bb, ax.transData)
bbox_image = BboxImage(tbb)
bbox_image.set_data(image_data)
ax.add_artist(bbox_image)

plt.show()
