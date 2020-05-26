import pytest

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from checkboxLegend import checkboxLegend, VisibilityHandler
from matplotlib.legend_handler import HandlerLine2D
from matplotlib.legend import Legend


class ExampleHandler:
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans):
        patch = mpatches.Rectangle([-xdescent, -ydescent], width, height, facecolor='red',
                                   edgecolor='black', hatch='xx', lw=3,
                                   transform=trans)
        return [patch]


def test_checkbox_legend_handler_map_unspecified():
    line1,  = plt.plot([1, 2], [1, 2], color='r', lw=2)
    legend = checkboxLegend(plt, [line1], ["R"])

    assert isinstance(legend.get_legend_handler(
        legend.get_legend_handler_map(), line1), VisibilityHandler)
    assert isinstance(legend.get_legend_handler(
        legend.get_legend_handler_map(), line1).handler, HandlerLine2D)


def test_checkbox_legend_handler_map_specified():
    line1,  = plt.plot([1, 2], [1, 2], color='r', lw=2)
    handler_map = {line1: ExampleHandler()}
    legend = checkboxLegend(plt, [line1], ["R"], handler_map=handler_map)
    assert isinstance(legend.get_legend_handler_map()
                      [line1], VisibilityHandler)
    assert isinstance(legend.get_legend_handler_map()
                      [line1].handler, ExampleHandler)


def test_checkbox_legend_no_handle_or_label():
    line1,  = plt.plot([1, 2], [1, 2], color='r', lw=2)
    legend = checkboxLegend(plt)

    assert isinstance(legend.get_legend_handler(
        legend.get_legend_handler_map(), line1), VisibilityHandler)
    assert isinstance(legend.get_legend_handler(
        legend.get_legend_handler_map(), line1).handler, HandlerLine2D)


def test_checkbox_legend_no_handle():
    line1,  = plt.plot([1, 2], [1, 2], color='r', lw=2)
    legend = checkboxLegend(plt, ["R"])

    assert isinstance(legend.get_legend_handler(
        legend.get_legend_handler_map(), line1), VisibilityHandler)
    assert isinstance(legend.get_legend_handler(
        legend.get_legend_handler_map(), line1).handler, HandlerLine2D)


def test_checkbox_legend_default_handler_set():
    line1,  = plt.plot([1, 2], [1, 2], color='r', lw=2)
    handler_map = {line1: ExampleHandler()}
    Legend.set_default_handler_map(handler_map)
    legend = checkboxLegend(plt, [line1], ["R"], fontsize=16)
    assert isinstance(legend.get_legend_handler_map()
                      [line1], VisibilityHandler)
    assert isinstance(legend.get_legend_handler_map()
                      [line1].handler, ExampleHandler)
