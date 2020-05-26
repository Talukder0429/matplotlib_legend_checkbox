import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerBase
from matplotlib.transforms import Bbox, TransformedBbox
from matplotlib.image import BboxImage
from matplotlib.legend import Legend
from pathlib import Path


class VisibilityHandler(HandlerBase):
    """
    A legend handler that shows checkboxes corresponding to handel
    visibility in the legend entry.
    """
    # static checked and unchecked boxes
    _checked = plt.imread(Path.cwd() / "checked.png")
    _unchecked = plt.imread(Path.cwd() / "unchecked.png")

    def __init__(self, handler=None):
        # init attributes
        self.handler = handler
        self.state = None
        super(VisibilityHandler, self).__init__()

    def legend_artist(self, legend, orig_handle, fontsize, handlebox):
        # shrink the gap between checkbox and label if needed
        if (self.handler is None):
            handlebox.set_width(handlebox.height)

        return super(VisibilityHandler, self).legend_artist(
            legend, orig_handle, fontsize, handlebox)

    def create_artists(self, legend, orig_handle, xdescent,
                       ydescent, width, height, fontsize, trans):
        # save original visibility and then make it visible
        orig_vis = orig_handle.get_visible()
        orig_handle.set_visible(1)
        # set correct state and image data
        if not orig_vis:
            image_data = VisibilityHandler._unchecked
            self.state = False
        else:
            image_data = VisibilityHandler._checked
            self.state = True

        # ratio for square checkbox
        image_ratio = image_data.shape[1] / image_data.shape[0]

        # create a checkbox artist
        bb = Bbox.from_bounds(xdescent, ydescent, height * image_ratio, height)
        tbb = TransformedBbox(bb, trans)
        image = BboxImage(tbb)
        image.set_data(image_data)

        # update self
        self.update_prop(image, orig_handle, legend)
        self.set_events(image, orig_handle)

        # artists to be returned
        artists = [image]

        # if a handler is given, create artists to be return
        if self.handler is not None:
            artists += self.handler.create_artists(
                legend, orig_handle, xdescent - (height * 2.), ydescent,
                width - (height * 2.), height, fontsize, trans)

        # revert visibility
        orig_handle.set_visible(orig_vis)
        return artists

    def is_checked(self):
        """
        Returns true if checked, false otherwise.
        """
        return self.state

    def set_events(self, bbox, orig_handle):
        # swaps checkbox status
        def onclick(event):
            if event.button == 1 and bbox.contains(event)[0]:
                if orig_handle.get_visible():
                    orig_handle.set_visible(False)
                    bbox.set_data(VisibilityHandler._unchecked)
                    self.state = False
                else:
                    orig_handle.set_visible(True)
                    bbox.set_data(VisibilityHandler._checked)
                    self.state = True
                plt.gcf().canvas.draw()
        plt.gcf().canvas.mpl_connect('button_press_event', onclick)

        # matches checkbox status to visibility
        def on_prop_change(artist):
            if artist.get_visible():
                bbox.set_data(VisibilityHandler._checked)
                self.state = True
            else:
                bbox.set_data(VisibilityHandler._unchecked)
                self.state = False
        orig_handle.add_callback(on_prop_change)


def checkboxLegend(parent, *args, **kwargs):
    """
    Creates a Legend with checkboxes to toggle visibility of all
    elements corresponding to entries in the legend

    Parameters
    ----------
    parent : `~matplotlib.axes.Axes` or `.Figure`
        The artist that contains the legend.
    """
    # get user genarated handler_map, and set handlelength to a default of 3
    custom_handler_map = kwargs.get('handler_map', {})
    if kwargs.get('handlelength', None) is None:
        kwargs['handlelength'] = 3

    # update a default handler map to include user genarated handler_map
    hm = Legend.get_default_handler_map().copy()
    hm.update(custom_handler_map)

    # create interactive version of the new handler map
    for handler in hm:
        hm[handler] = VisibilityHandler(
            handler=Legend.get_legend_handler(hm, handler))
    kwargs['handler_map'] = hm

    # return interactive legend
    return parent.legend(*args, **kwargs)
