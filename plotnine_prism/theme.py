"""Provides theme_prism"""
from plotnine.options import get_option
from plotnine.themes.elements import (
    element_blank,
    element_line,
    element_rect,
    element_text,
)
from plotnine.themes.theme import theme as theme_abc

from .pal import list_themes, theme_colors

# Make sure the themeables work
from .themeable import (  # noqa: F401
    axis_ticks_x,
    axis_ticks_y,
    prism_ticks_length,
    prism_ticks_length_x,
    prism_ticks_length_y,
)


class theme_prism(theme_abc):
    """The theme_prism() class

    Args:
        palette: The theme palette
        base_size: The base size of the plot
        base_family: The base font family
        base_fontface: The base font face
        base_line_size: The base line size
        base_rect_size: The base rect size
        axis_text_angle: The default axis text angle
        border: Whether to show border of the plot
        **kwargs: Other theming options
    """

    def __init__(
        self,
        palette="black_and_white",
        base_size=10.0,
        base_family="DejaVu Sans",
        base_fontface="bold",
        base_line_size=None,
        base_rect_size=None,
        axis_text_angle=0,
        border=False,
        **kwargs,
    ):
        """Construct"""
        if axis_text_angle not in (0, 45, 90, 270):
            raise ValueError(
                "'axis_text_angle' must be one of [0, 45, 90, 270].\n"
                "For other angles, use `guide_axis()` function from plotnine "
                "instead"
            )

        if palette not in list_themes():
            raise ValueError(
                f"The palette '{palette}' does not exist. "
                f"Supported palettes are: {list_themes()}"
            )

        if base_line_size is None:
            base_line_size = base_size / 14.0
        if base_rect_size is None:
            base_rect_size = base_size / 14.0

        colours = theme_colors(palette)
        if border:
            panel_border = element_rect(fill=None)
            axis_line = element_blank()
        else:
            panel_border = element_blank()
            axis_line = element_line()

        m = get_option("base_margin")
        kwargs.setdefault("line", element_line(
            colour=colours.axisColor,
            size=base_line_size,
            linetype="solid",
            lineend="butt",
        ))
        kwargs.setdefault("rect", element_rect(
            fill="white",
            colour=colours.axisColor,
            size=base_rect_size,
            linetype="solid",
        ))
        kwargs.setdefault("text", element_text(
            family=base_family,
            face=base_fontface,
            colour=colours.graphTitleColor,
            size=base_size,
            lineheight=0.9,
            hjust=0.5,
            vjust=0.5,
            angle=0,
            margin={},
        ))
        kwargs.setdefault("dpi", get_option("dpi"))
        kwargs.setdefault("figure_size", get_option("figure_size"))
        kwargs.setdefault("prism_ticks_length", base_size / 5)
        kwargs.setdefault("axis_line", axis_line)
        kwargs.setdefault("axis_line_x", None)
        kwargs.setdefault("axis_line_y", None)
        kwargs.setdefault("axis_text", element_text(
            size=0.95 * base_size,
            colour=colours.axisLabelColor,
        ))
        kwargs.setdefault("axis_text_x", element_text(
            margin={"t": 0.8 * base_size},
            angle=axis_text_angle,
            hjust=2 if axis_text_angle in (45, 90, 270) else 0.5,
            vjust=0.5 if axis_text_angle in (0, 90, 270) else 1,
        ))
        kwargs.setdefault("axis_text_y", element_text(
            margin={"r": 0.2 * base_size},
            hjust=1,
        ))
        kwargs.setdefault("axis_ticks", element_line())
        kwargs.setdefault("axis_ticks_length", base_size / 2.5)
        kwargs.setdefault("axis_title", element_text(
            colour=colours.axisTitleColor,
        ))
        kwargs.setdefault("axis_title_x", element_text())
        kwargs.setdefault("axis_title_y", element_text(
            margin={"r": .5 * base_size},
            angle=90,
        ))
        kwargs.setdefault("legend_background", element_rect(
            fill="None",
            colour="None",
        ))
        kwargs.setdefault("legend_entry_spacing_x", 5)
        kwargs.setdefault("legend_entry_spacing_y", 2)
        kwargs.setdefault("legend_key", element_rect(
            fill="None",
            colour="None",
        ))
        kwargs.setdefault("legend_key_size", base_size * 0.8 * 1.8)
        kwargs.setdefault("legend_key_height", 8.5)
        kwargs.setdefault("legend_key_width", base_size * 1.5)
        kwargs.setdefault("legend_margin", 0)  # points
        kwargs.setdefault("legend_spacing", base_size)  # points
        kwargs.setdefault("legend_text", element_text(
            size=base_size * 0.75,
            ha="left",
            weight="normal",
            margin={"t": 3, "b": 3, "l": 3, "r": 3, "units": "pt"},
        ))
        kwargs.setdefault("legend_text_legend", element_text(
            va="baseline",
            weight="normal",
        ))
        kwargs.setdefault("legend_text_colorbar", element_text(
            va="center",
            weight="normal",
        ))
        kwargs.setdefault("legend_title", element_blank())
        kwargs.setdefault("legend_title_align", "auto")
        kwargs.setdefault("legend_position", "right")
        kwargs.setdefault("legend_box", "auto")
        kwargs.setdefault("legend_box_margin", 0)  # points
        kwargs.setdefault("legend_box_just", "auto")
        kwargs.setdefault("legend_box_spacing", 0.1)  # In inches
        kwargs.setdefault("legend_direction", "vertical")
        kwargs.setdefault("aspect_ratio", "auto")
        kwargs.setdefault("strip_align", 0)
        kwargs.setdefault("strip_align_x", 0)
        kwargs.setdefault("panel_background", element_rect(
            fill=colours.plottingAreaColor if palette == "office" else "None",
            colour=None,
        ))
        kwargs.setdefault("panel_border", panel_border)
        kwargs.setdefault("panel_grid", element_blank())
        kwargs.setdefault("panel_grid_minor", element_blank())
        kwargs.setdefault("panel_spacing", 4 * base_size / 3.0)
        kwargs.setdefault("panel_spacing_x", None)
        kwargs.setdefault("panel_spacing_y", None)
        kwargs.setdefault("panel_ontop", False)
        kwargs.setdefault("strip_background", element_blank())
        kwargs.setdefault("strip_text", element_text(
            colour=colours.axisTitleColor,
            # size = rel(0.8),
            size=0.8 * base_size,
            margin={
                "t": base_size / 2.5,
                "b": base_size / 2.5,
                "l": base_size / 2.5,
                "r": base_size / 2.5,
            },
        ))
        kwargs.setdefault("strip_text_x", element_text(
            margin={"t": base_size / 3},
        ))
        kwargs.setdefault("strip_text_y", element_text(
            angle=-90,
            margin={"l": base_size / 3},
        ))
        kwargs.setdefault("plot_background", element_rect(
            fill=colours.pageBackgroundColor,
            colour=colours.pageBackgroundColor,
        ))
        kwargs.setdefault("plot_title", element_text(
            size=1.2 * base_size,
            hjust=0.5,
            vjust=1,
            margin={"b": base_size},
        ))
        kwargs.setdefault("plot_caption", element_text(
            size=0.8,
            hjust=1,
            vjust=1,
            margin={"t": base_size / 2},
        ))
        kwargs.setdefault("plot_margin", m * 2)

        theme_abc.__init__(self, complete=True, **kwargs)
