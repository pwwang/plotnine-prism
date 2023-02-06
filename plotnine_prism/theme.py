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
        base_size=8.0,
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
            base_line_size = 4 / 3.0 * base_size / 10.0
        if base_rect_size is None:
            base_rect_size = 4 / 3.0 * base_size / 10.0

        colours = theme_colors(palette)
        if border:
            panel_border = element_rect(fill=None)
            axis_line = element_blank()
        else:
            panel_border = element_blank()
            axis_line = element_line()

        theme_abc.__init__(
            self,
            # Base elements (to be inherited by other elements)
            line=element_line(
                colour=colours.axisColor,
                size=base_line_size,
                linetype="solid",
                lineend="butt",
            ),
            rect=element_rect(
                fill="white",
                colour=colours.axisColor,
                size=base_rect_size,
                linetype="solid",
            ),
            text=element_text(
                family=base_family,
                face=base_fontface,
                colour=colours.graphTitleColor,
                size=base_size,
                lineheight=0.9,
                hjust=0.5,
                vjust=0.5,
                angle=0,
                margin={},
            ),
            # Options
            dpi=get_option("dpi"),
            figure_size=get_option("figure_size"),
            # Prism custom theme elements
            prism_ticks_length=base_size / 5,
            # Normal ggplot2 theme elements
            axis_line=axis_line,
            axis_line_x=None,
            axis_line_y=None,
            axis_text=element_text(
                size=0.95 * base_size, colour=colours.axisLabelColor
            ),
            axis_text_x=element_text(
                margin=dict(t=0.8 * base_size),
                angle=axis_text_angle,
                hjust=2 if axis_text_angle in (45, 90, 270) else 0.5,
                vjust=0.5 if axis_text_angle in (0, 90, 270) else 1,
            ),
            # axis_text_x_top=element_text(margin=dict(b=0.8 * base_size / 4),
            # vjust=0),
            axis_text_y=element_text(
                margin=dict(r=0.8 * base_size / 4), hjust=1
            ),
            # axis_text_y_right=element_text(
            # margin=dict(l=0.5 * base_size / 4),
            # hjust=0),
            axis_ticks=element_line(),
            # axis_ticks_length =  unit(base_size / 2.5, "pt"),
            axis_ticks_length=base_size / 2.5,
            # axis_ticks_length_x=None,
            # axis_ticks_length_x_top=None,
            # axis_ticks_length_x_bottom=None,
            # axis_ticks_length_y=None,
            # axis_ticks_length_y_top=None,
            # axis_ticks_length_y_bottom=None,
            axis_title=element_text(colour=colours.axisTitleColor),
            axis_title_x=element_text(margin=dict(t=base_size * 0.6), vjust=1),
            # axis_title_x_top=element_text(margin=dict(b=base_size * 0.6),
            # vjust=0),
            axis_title_y=element_text(
                angle=90, margin=dict(r=base_size * 1.5), vjust=1
            ),
            # axis_title_y_right=element_text(
            #     angle=-90, margin=dict(l=base_size * 0.6), vjust=0
            # ),
            # legend
            legend_background=element_rect(color="None", fill="None"),
            legend_entry_spacing_x=5,
            legend_entry_spacing_y=2,
            legend_key=element_rect(colour="None", fill="None"),
            legend_key_size=base_size * 0.8 * 1.8,
            legend_key_height=8.5,
            legend_key_width=base_size * 1.5,
            legend_margin=0,  # points
            legend_spacing=base_size,  # points
            legend_text=element_text(
                size=base_size * 0.75,
                ha="left",
                weight="normal",
                margin={"t": 3, "b": 3, "l": 3, "r": 3, "units": "pt"},
            ),
            legend_text_legend=element_text(va="baseline", weight="normal"),
            legend_text_colorbar=element_text(va="center", weight="normal"),
            legend_title=element_blank(),
            legend_title_align="auto",
            legend_position="right",
            legend_box="auto",
            legend_box_margin=0,  # points
            legend_box_just="auto",
            legend_box_spacing=0.1,  # In inches
            legend_direction="vertical",
            aspect_ratio="auto",
            strip_margin=0,
            strip_margin_x=0,
            panel_background=element_rect(
                fill=colours.plottingAreaColor
                if palette == "office"
                else "None",
                colour=None,
            ),
            panel_border=panel_border,
            panel_grid=element_blank(),
            panel_grid_minor=element_blank(),
            # panel_spacing =      unit(base_size / 2, "pt"),
            panel_spacing=4 * base_size / 3.0,
            panel_spacing_x=None,
            panel_spacing_y=None,
            panel_ontop=False,
            strip_background=element_blank(),
            strip_text=element_text(
                colour=colours.axisTitleColor,
                # size = rel(0.8),
                size=0.8 * base_size,
                margin=dict(
                    t=base_size / 2.5,
                    b=base_size / 2.5,
                    l=base_size / 2.5,
                    r=base_size / 2.5,
                ),
            ),
            strip_text_x=element_text(margin=dict(b=base_size / 3)),
            strip_text_y=element_text(angle=-90, margin=dict(l=base_size / 3)),
            # strip_text_y_left=element_text(angle=90),
            # strip_placement="inside",
            # strip_placement_x=None,
            # strip_placement_y=None,
            # strip_switch_pad_grid = unit(base_size / 4, "pt"),
            # strip_switch_pad_wrap = unit(base_size / 4, "pt"),
            # strip_switch_pad_grid=base_size / 4,
            # strip_switch_pad_wrap=base_size / 4,
            plot_background=element_rect(
                fill=colours.pageBackgroundColor,
                colour=colours.pageBackgroundColor,
            ),
            # plot_title =         element_text(size = rel(1.2),
            plot_title=element_text(
                size=1.2 * base_size,
                hjust=0.5,
                vjust=1,
                margin=dict(b=base_size),
            ),
            # plot_title_position="panel",
            # plot_subtitle=element_text(
            #     hjust=0.5, vjust=1, margin=dict(b=base_size / 2)
            # ),
            # plot_caption =       element_text(size = rel(0.8),
            plot_caption=element_text(
                size=0.8, hjust=1, vjust=1, margin=dict(t=base_size / 2)
            ),
            # plot_caption_position="panel",
            # plot_tag =           element_text(size = rel(1.2),
            # plot_tag=element_text(size=1.2, hjust=0.5, vjust=0.5),
            # plot_tag_position="topleft",
            # plot_margin=base_size / 2,
            plot_margin=None,
            complete=True,
            **kwargs,
        )
