import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerBase
from matplotlib.transforms import Bbox, TransformedBbox
from matplotlib.image import BboxImage
from matplotlib.offsetbox import DrawingArea
from matplotlib.legend import Legend
from pathlib import Path


class VisibilityHandler(HandlerBase):
    _checked = plt.imread(Path.cwd() / "checked.png")
    _unchecked = plt.imread(Path.cwd() / "unchecked.png")

    def __init__(self, handler=None):
        # init attributes
        self.handler = handler
        super(VisibilityHandler, self).__init__()

    def legend_artist(self, legend, orig_handle, fontsize, handlebox):
        # save original visibility, enable visible and set correct checkbox status
        orig_vis = orig_handle.get_visible()
        orig_handle.set_visible(1)
        if not orig_vis:
            image_data = VisibilityHandler._unchecked
        else:
            image_data = VisibilityHandler._checked
        image_ratio = image_data.shape[1] / image_data.shape[0]

        # get dimensions
        x0, y0 = handlebox.xdescent, handlebox.ydescent
        width, height = handlebox.width, handlebox.height
        trans = handlebox.get_transform()

        # create and setup a checkbox image container, then add to handlebox
        bb = Bbox.from_bounds(x0, y0, height * image_ratio, height)
        tbb = TransformedBbox(bb, trans)
        image = BboxImage(tbb)

        image.set_data(image_data)
        self.update_prop(image, orig_handle, legend)
        self.set_events(image, orig_handle)
        handlebox.add_artist(image)

        # if a handler is given, create a container for it and add to handlebox
        if self.handler is not None:
            da = DrawingArea(width / 2., height, x0 - width/2., y0)
            artist = self.handler.legend_artist(
                legend, orig_handle, fontsize, da)
            artist.set_transform(trans)
            handlebox.add_artist(da)

        # revert visibility
        orig_handle.set_visible(orig_vis)
        return image

    @classmethod
    def set_events(cls, bbox, orig_handle):
        def onclick(event):
            if event.button == 1 and bbox.contains(event)[0]:
                if orig_handle.get_visible():
                    orig_handle.set_visible(False)
                    bbox.set_data(cls._unchecked)
                else:
                    orig_handle.set_visible(True)
                    bbox.set_data(cls._checked)
                plt.gcf().canvas.draw()
        plt.gcf().canvas.mpl_connect('button_press_event', onclick)

        def ondraw(event):
            if orig_handle.get_visible():
                bbox.set_data(cls._checked)
            else:
                bbox.set_data(cls._unchecked)
        plt.gcf().canvas.mpl_connect('draw_event', ondraw)


def checkboxLegend(parent, handles=None, labels=None, handler_map=None, handlelength=3, **kwargs):
    # set update default handlers with given handlers
    if handler_map is not None:
        Legend.update_default_handler_map(handler_map)

    # if no handles were given, fetch all legend handles
    if handles is None:
        ax = plt.gca()
        handles, labels = ax.get_legend_handles_labels()

    # use our handler for given handles
    hm = {}
    for handle in handles:
        default_handler = Legend.get_legend_handler(
            Legend.get_default_handler_map(), handle)
        hm[handle] = VisibilityHandler(handler=default_handler)

    legend = parent.legend(handles, labels, handler_map=hm,
                        handlelength=handlelength, **kwargs)
    return legend
