"""Prism themes for plotnine, inspired by ggprism"""

from .theme import theme_prism
from .scale import (
    scale_color_prism,
    scale_fill_prism,
    scale_shape_prism,
    scale_colour_prism,
)
from .pal import (
    list_themes,
    list_color_pals,
    list_colour_pals,
    list_fill_pals,
    list_shape_pals,
    prism_color_pal,
    prism_colour_pal,
    prism_fill_pal,
    prism_shape_pal,
)
from .guide import (
    guide_prism,
    guide_prism_minor,
    # guide_prism_bracket,
    guide_prism_offset,
    guide_prism_offset_minor,
)

__all__ = (
    "theme_prism",
    "scale_color_prism",
    "scale_colour_prism",
    "scale_fill_prism",
    "scale_shape_prism",
    "list_themes",
    "list_color_pals",
    "list_colour_pals",
    "list_fill_pals",
    "list_shape_pals",
    "prism_color_pal",
    "prism_colour_pal",
    "prism_fill_pal",
    "prism_shape_pal",
    "guide_prism",
    "guide_prism_minor",
    # "guide_prism_bracket",
    "guide_prism_offset",
    "guide_prism_offset_minor",
)

__version__ = "0.2.0"
