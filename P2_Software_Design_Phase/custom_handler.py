import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches


class DemoHandler():
    def legend_artist(self, legend, orig_handle, fontsize, handlebox):
        # getting dimensions
        x0, y0 = handlebox.xdescent, handlebox.ydescent
        width, height = handlebox.width, handlebox.height
        trans = handlebox.get_transform()

        # creating a line object, and placing it appropriately
        line = mlines.Line2D(
            [x0, x0+width/2], [y0+height/2., y0+height/2.], transform=trans)

        # creating a patch object, and placing it appropriately
        patch = mpatches.Rectangle(
            [x0+width/2. + fontsize/2, y0], width/2., height, facecolor='red', edgecolor='black', lw=1, transform=trans)

        # adding the line and patch to the handler
        handlebox.add_artist(line)
        handlebox.add_artist(patch)
        return [line, patch]


line,  = plt.plot([1, 2], [1, 2])
plt.legend([line], [""], handler_map={line: DemoHandler()}, fontsize=24)
plt.show()
