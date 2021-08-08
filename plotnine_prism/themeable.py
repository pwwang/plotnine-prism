from contextlib import suppress
from copy import deepcopy
from plotnine.themes.themeable import themeable as themeable_abc

class prism_ticks_length_x(themeable_abc):

    def apply(self, ax):
        themeable_abc.apply(self, ax)

        d = deepcopy(self.properties)
        with suppress(KeyError):
            ax.xaxis.set_tick_params(which='minor', length=d.pop('value'))

        for tick in ax.xaxis.get_minor_ticks():
            tick.tick1line.set(**d)

    def blank(self, ax):
        themeable_abc.blank(self, ax)
        ax.xaxis.set_tick_params(which='minor', bottom=False)

class prism_ticks_length_y(themeable_abc):

    def apply(self, ax):
        themeable_abc.apply(self, ax)

        d = deepcopy(self.properties)
        with suppress(KeyError):
            ax.yaxis.set_tick_params(which='minor', length=d.pop('value'))

        for tick in ax.yaxis.get_minor_ticks():
            tick.tick1line.set(**d)

    def blank(self, ax):
        themeable_abc.blank(self, ax)
        ax.yaxis.set_tick_params(which='minor', bottom=False)

class prism_ticks_length(prism_ticks_length_x, prism_ticks_length_y):

    def apply(self, ax):
        prism_ticks_length_x.apply(self, ax)
        prism_ticks_length_y.apply(self, ax)

    def blank(self, ax):
        prism_ticks_length_x.blank(self, ax)
        prism_ticks_length_y.blank(self, ax)
