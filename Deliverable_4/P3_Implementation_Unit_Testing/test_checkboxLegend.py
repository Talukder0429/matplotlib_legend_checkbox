import pytest

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pytest_check as check
from checkboxLegend import VisibilityHandler


def test_checkboxLegend_patch():
    """Test legend with patches"""
    rect = mpatches.Rectangle((0, 0), 0.5, 0.5, label="rect")
    ax = plt.gca()
    ax.add_patch(rect)
    legend = plt.legend([rect], ["rect"], handler_map =  {rect: VisibilityHandler()})
    rect_handle = legend.get_legend_handler(legend.get_legend_handler_map(), rect)
    rect_handler = rect_handle.handler
    checked = rect_handle.is_checked()
    check.is_none(rect_handler)
    check.equal(checked, True)

def test_checkboxLegend_line():
    """Test legend with lines"""
    line,  = plt.plot([1, 2], [1, 2], color='r', lw=2)
    legend = plt.legend([line], ["line"], handler_map =  {line: VisibilityHandler()})
    line_handle = legend.get_legend_handler(legend.get_legend_handler_map(), line)
    line_handler = line_handle.handler
    checked = line_handle.is_checked()
    check.is_none(line_handler)
    check.equal(checked, True)

def test_checkboxLegend_text():
    """Test legend with text"""
    ax = plt.gca()
    line,  = plt.plot([1, 2], [1, 2], color='r', lw=2)
    text = plt.text(1, 1.5, "text on plot")
    legend = plt.legend([text], ["text"], handler_map =  {text: VisibilityHandler(handler=None)})
    text_handle = legend.get_legend_handler(legend.get_legend_handler_map(), text)
    text_handler = text_handle.handler
    checked = text_handle.is_checked()
    check.is_none(text_handler)
    check.equal(checked, True)

def test_checkboxLegend_multiple():
    """Test with multiple handlers"""
    ax = plt.gca()
    line,  = plt.plot([1, 2], [1, 2], color='r', lw=2)
    text = plt.text(1, 1.5, "text on plot")
    rect = mpatches.Rectangle((1.5, 1.4), 0.5, 0.5, label="rect")
    rect.set_visible(0)
    ax.add_patch(rect)
    legend = plt.legend([text, line, rect], ["text", "line", "rect"], handler_map =  {text: VisibilityHandler(),
                                             line: VisibilityHandler(), rect: VisibilityHandler()})
    line_handle = legend.get_legend_handler(legend.get_legend_handler_map(), line)
    line_handler = line_handle.handler
    rect_handle = legend.get_legend_handler(legend.get_legend_handler_map(), rect)
    rect_handler = rect_handle.handler
    line_checked = line_handle.is_checked()
    rect_checked = rect_handle.is_checked()
    text_handle = legend.get_legend_handler(legend.get_legend_handler_map(), text)
    text_handler = text_handle.handler
    text_checked = text_handle.is_checked()                                
    check.is_none(line_handler)
    check.is_none(rect_handler)
    check.is_none(text_handler)
    check.equal(line_checked, True)
    check.equal(rect_checked, False)
    check.equal(text_checked, True)

class ExampleHandler:
    def create_artists(self, legend, orig_handle,
                       xdescent, ydescent, width, height, fontsize, trans):
        patch = mpatches.Rectangle([-xdescent, -ydescent], width, height, facecolor='blue',
                                   edgecolor='black', lw=2,
                                   transform=trans)
        patch.set_transform(trans)
        return [patch]

def test_checkboxLegend_customHandler():
    """Test legend with custom handler"""
    ax = plt.gca()
    line,  = plt.plot([1, 2], [1, 2], color='r', lw=2)
    custom_handler = ExampleHandler()
    legend = plt.legend([line], ["line"], handler_map={line: VisibilityHandler(handler=custom_handler)})
    handler = legend.get_legend_handler(legend.get_legend_handler_map(), line).handler
    check.equal(custom_handler, handler)

def test_checkboxLegend_itself():
    """Test legend with handler as itself"""
    ax = plt.gca()
    line,  = plt.plot([1, 2], [1, 2], color='r', lw=2)
    itself = VisibilityHandler()
    legend = plt.legend([line], ["line"], handler_map={line: VisibilityHandler(handler=itself)})
    handler = legend.get_legend_handler(legend.get_legend_handler_map(), line).handler
    check.equal(itself, handler)

def test_checkboxLegend_visibility_before():
    """Test legend with visibility off before adding to the handler map"""
    rect = mpatches.Rectangle((0, 0), 0.5, 0.5)
    ax = plt.gca()
    ax.add_patch(rect)
    rect.set_visible(0)
    legend = plt.legend([rect], ["rect"], handler_map =  {rect: VisibilityHandler()})
    handle = legend.get_legend_handler(legend.get_legend_handler_map(), rect)
    checked = handle.is_checked()
    check.equal(checked, False)

def test_checkboxLegend_visibility_after():
    """Test legend with visibility off after adding to the handler map"""
    fig = plt.figure()
    rect = mpatches.Rectangle((0, 0), 0.5, 0.5)
    ax = plt.gca()
    ax.add_patch(rect)
    legend = plt.legend([rect], ["rect"], handler_map =  {rect: VisibilityHandler()})
    rect.set_visible(0)
    fig.canvas.draw()
    handle = legend.get_legend_handler(legend.get_legend_handler_map(), rect)
    checked = handle.is_checked()
    check.equal(checked, False)
