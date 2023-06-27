"""Provides scales"""

from plotnine.exceptions import PlotnineError
from plotnine.scales.scale import scale_discrete, scale_continuous
from .pal import prism_color_pal, prism_fill_pal, prism_shape_pal


def get_minor_breaks(
    self,
    major,
    limits=None,
):
    """
    Return minor breaks

    See https://github.com/has2k1/plotnine/issues/696
    """
    if limits is None:
        limits = self.limits

    if self.minor_breaks is True:
        # TODO: Remove ignore when mizani is static typed
        minor_breaks = self.trans.minor_breaks(
            major, limits
        )  # pyright: ignore
    elif isinstance(self.minor_breaks, int):
        # TODO: Remove ignore when mizani is static typed
        minor_breaks = self.trans.minor_breaks(
            major, limits, n=self.minor_breaks
        )  # pyright: ignore
    elif (
        self.minor_breaks is False
        or self.minor_breaks is None
        or not len(major)
    ):
        minor_breaks = []
    elif callable(self.minor_breaks):
        breaks = self.minor_breaks(self.trans.inverse(limits))
        _major = set(major)
        minor = self.trans.transform(breaks)
        minor_breaks = [x for x in minor if x not in _major]
    else:
        minor_breaks = self.trans.transform(self.minor_breaks)

    return minor_breaks


def get_labels(
    self, breaks=None
):
    """
    Generate labels for the axis or legend

    Parameters
    ----------
    breaks: None or array-like
        If None, use self.breaks.
    """
    if breaks is None:
        breaks = self.get_breaks()

    breaks = self.inverse(breaks)

    if self.labels is True:
        labels = self.trans.format(breaks)
    elif self.labels is False or self.labels is None:
        labels = []
    elif callable(self.labels):
        labels = self.labels(breaks)
    elif isinstance(self.labels, dict):
        labels = [
            str(self.labels[b]) if b in self.labels else str(b)
            for b in breaks
        ]
    else:
        # When user sets breaks and labels of equal size,
        # but the limits exclude some of the breaks.
        # We remove the corresponding labels
        from collections.abc import Sized

        labels = self.labels
        if (
            len(labels) != len(breaks)
            and isinstance(self.breaks, Sized)
            and len(labels) == len(self.breaks)
        ):
            _wanted_breaks = set(breaks)
            labels = [
                lab
                for lab, b in zip(labels, self.breaks)
                if b in _wanted_breaks
            ]

    if len(labels) != len(breaks):
        raise PlotnineError("Breaks and labels are different lengths")

    return labels


# Patch scale_continuous to fix #696
scale_continuous.get_minor_breaks = get_minor_breaks
scale_continuous.get_labels = get_labels


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
