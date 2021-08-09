from contextlib import suppress
from copy import deepcopy
from plotnine.themes.themeable import (
    themeable as themeable_abc,
    axis_ticks_major_x,
    axis_ticks_major_y,
    axis_ticks_minor_x,
    axis_ticks_minor_y,
)

class axis_ticks_x(axis_ticks_major_x, axis_ticks_minor_x):
    def apply(self, ax):
        axis_ticks_major_x.apply(self, ax)
        axis_ticks_minor_x.apply(self, ax)

    def blank(self, ax):
        axis_ticks_major_x.blank(self, ax)
        axis_ticks_minor_x.blank(self, ax)


class axis_ticks_y(axis_ticks_major_y, axis_ticks_minor_y):
    def apply(self, ax):
        axis_ticks_major_y.apply(self, ax)
        axis_ticks_minor_y.apply(self, ax)

    def blank(self, ax):
        axis_ticks_major_y.blank(self, ax)
        axis_ticks_minor_y.blank(self, ax)



class prism_ticks_length_x(themeable_abc):
    def apply(self, ax):
        themeable_abc.apply(self, ax)

        d = deepcopy(self.properties)
        with suppress(KeyError):
            length = d.pop("value")
            ax.xaxis.set_tick_params(
                which="minor",
                length=abs(length),
                direction="in" if length < 0 else "out",
            )

        for tick in ax.xaxis.get_minor_ticks():
            tick.tick1line.set(**d)

    def blank(self, ax):
        themeable_abc.blank(self, ax)
        ax.xaxis.set_tick_params(which="minor", bottom=False)


class prism_ticks_length_y(themeable_abc):
    def apply(self, ax):
        themeable_abc.apply(self, ax)

        d = deepcopy(self.properties)
        with suppress(KeyError):
            length = d.pop("value")
            ax.yaxis.set_tick_params(
                which="minor",
                length=abs(length),
                direction="in" if length < 0 else "out",
            )

        for tick in ax.yaxis.get_minor_ticks():
            tick.tick1line.set(**d)

    def blank(self, ax):
        themeable_abc.blank(self, ax)
        ax.yaxis.set_tick_params(which="minor", bottom=False)


class prism_ticks_length(prism_ticks_length_x, prism_ticks_length_y):
    def apply(self, ax):
        prism_ticks_length_x.apply(self, ax)
        prism_ticks_length_y.apply(self, ax)

    def blank(self, ax):
        prism_ticks_length_x.blank(self, ax)
        prism_ticks_length_y.blank(self, ax)
