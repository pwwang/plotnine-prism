"""Provides scales"""

from plotnine.scales.scale import scale_discrete
from .pal import prism_color_pal, prism_fill_pal, prism_shape_pal


class scale_color_prism(scale_discrete):
    """Prism color scale

    Args:
        palette: The color palette name
    """

    _aesthetics = ["color"]
    na_value = "#7F7F7F"

    def __init__(self, palette="colors", **kwargs):
        """Construct"""
        self.palette = prism_color_pal(palette)
        scale_discrete.__init__(self, **kwargs)


class scale_fill_prism(scale_color_prism):
    """Prism fill scale

    Args:
        palette: The fill palette name
    """

    _aesthetics = ["fill"]
    na_value = "#7F7F7F"

    def __init__(self, palette="colors", **kwargs):
        """Construct"""
        self.palette = prism_fill_pal(palette)
        scale_discrete.__init__(self, **kwargs)


class scale_shape_prism(scale_discrete):
    """Prism shape scale

    Args:
        palette: The shape palette name
    """

    _aesthetics = ["shape"]

    def __init__(self, palette="default", **kwargs):
        """Construct"""
        self.palette = prism_shape_pal(palette)
        scale_discrete.__init__(self, **kwargs)


scale_colour_prism = scale_color_prism
