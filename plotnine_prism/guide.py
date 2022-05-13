"""Provides guides"""
import hashlib
from warnings import warn

from matplotlib.ticker import NullLocator

from plotnine.guides.guide import guide
from plotnine.exceptions import PlotnineWarning


class guide_prism_offset(guide):
    """The prism offset guide that offset the axes"""

    offset = 20
    aesthetic = None
    hash = None
    available_aes = {"x", "y"}

    def train(self, scale, aesthetic=None):
        """Get arguments from the scale"""
        if aesthetic is None:
            aesthetic = scale.aesthetics[0]

        # Do nothing if scales are inappropriate
        if set(scale.aesthetics) & self.available_aes == 0:
            warn(
                f"'{self.__class__.__name__}' needs appropriate scales.",
                PlotnineWarning,
            )
            return None

        self.aesthetic = list(set(scale.aesthetics) & self.available_aes)[0]

        info = "\n".join([self.title, self.__class__.__name__])
        self.hash = hashlib.md5(info.encode("utf-8")).hexdigest()
        return self

    def create_geoms(self, plot):
        """Apply the arguments"""
        xaxis_position = plot.axs[0].xaxis.get_label_position()
        yaxis_position = plot.axs[0].yaxis.get_label_position()
        gca = plot.axs[0].axes

        if self.aesthetic == "x":
            major_locs = gca.get_xticks()
            minor_locs = gca.xaxis.get_minorticklocs()
            if yaxis_position == "left":
                offset = (
                    self.offset
                    if major_locs[0] > minor_locs[0]
                    else self.offset / 2
                )
            else:
                offset = (
                    self.offset
                    if major_locs[-1] < minor_locs[-1]
                    else self.offset / 2
                )
            gca.spines[yaxis_position].set_position(("outward", offset))
            gca.set_xlim(min(major_locs), max(major_locs))
            gca.xaxis.set_minor_locator(NullLocator())
        else:
            major_locs = gca.get_yticks()
            minor_locs = gca.yaxis.get_minorticklocs()
            if xaxis_position == "bottom":
                offset = (
                    self.offset
                    if major_locs[0] > minor_locs[0]
                    else self.offset / 2
                )
            else:
                offset = (
                    self.offset
                    if major_locs[-1] < minor_locs[-1]
                    else self.offset / 2
                )
            gca.spines[xaxis_position].set_position(("outward", offset))
            gca.set_ylim(min(major_locs), max(major_locs))
            gca.yaxis.set_minor_locator(NullLocator())

    def merge(self, other):
        """Simply discards the other guide"""
        return self

    def draw(self):
        """Nothing to do"""


class guide_prism(guide_prism_offset):
    """The prism offset guide that hides the minor ticks"""

    available_aes = {"x", "y"}

    def create_geoms(self, plot):
        """Apply the arguments"""
        gca = plot.axs[0].axes
        if self.aesthetic == "x":
            gca.xaxis.set_minor_locator(NullLocator())
        else:
            gca.yaxis.set_minor_locator(NullLocator())


class guide_prism_minor(guide_prism_offset):
    """The prism offset guide that shows the minor ticks"""

    available_aes = {"x", "y"}

    def create_geoms(self, plot):
        """Apply the arguments"""


class guide_prism_offset_minor(guide_prism_offset):
    """The prism offset guide that shows the minor ticks with offset"""

    def create_geoms(self, plot):
        """Apply the arguments"""
        xaxis_position = plot.axs[0].xaxis.get_label_position()
        yaxis_position = plot.axs[0].yaxis.get_label_position()
        gca = plot.axs[0].axes

        if self.aesthetic == "x":
            gca.spines[yaxis_position].set_position(("outward", self.offset))
            major_locs = gca.get_xticks()
            minor_locs = gca.xaxis.get_minorticklocs()
            min_loc = min(min(major_locs), min(minor_locs))
            max_loc = max(max(major_locs), max(minor_locs))
            gca.set_xlim(min_loc, max_loc)
        else:
            gca.spines[xaxis_position].set_position(("outward", self.offset))
            major_locs = gca.get_yticks()
            minor_locs = gca.yaxis.get_minorticklocs()
            min_loc = min(min(major_locs), min(minor_locs))
            max_loc = max(max(major_locs), max(minor_locs))
            gca.set_ylim(min_loc, max_loc)


# class AxesBracketDecorator:
#     def __init__(self, ax, ticks, size="5%", pad=0.05, spacing=0.05):

#         divider = make_axes_locatable(ax)
#         self.ax = divider.new_vertical(
#             size=size,
#             pad=pad,
#             sharex=ax,
#             pack_start=True,
#         )
#         ax.figure.add_axes(self.ax)
#         ax.xaxis.set_visible(False)
#         # ax.xaxis.spines['bottom'].set_visible(False)
#         # self.ax.tick_params(axis='x', which=u'both', length=0)
#         for direction in ["left", "right", "bottom", "top"]:
#             self.ax.spines[direction].set_visible(False)
#         self.ax.set_yticks([])
#         pos = self.ax.get_position()

#         self.dist = numpy.mean(numpy.diff(ticks))
#         self.spacing = spacing
#         # self.curve = self.get_curve()
#         for tick in ticks:
#             # self.plot_curve(tick)
#             pass


# class guide_prism_bracket(guide_prism_offset):

#     def create_geoms(self, plot):
#         gca = plot.axs[0].axes
#         if self.aesthetic == "x":
#             AxesBracketDecorator(gca, ticks=gca.get_xticks())
#         else:
#             AxesBracketDecorator(gca, ticks=gca.get_yticks())
