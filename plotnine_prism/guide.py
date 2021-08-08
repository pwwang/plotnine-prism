import hashlib
from warnings import warn

from plotnine.guides.guide import guide
from plotnine.exceptions import PlotnineWarning

class guide_prism_offset(guide):

    offset = 20
    aesthetic = None
    available_aes = {'x', 'y'}

    def train(self, scale, aesthetic=None):
        if aesthetic is None:
            aesthetic = scale.aesthetics[0]

        # Do nothing if scales are inappropriate
        if set(scale.aesthetics) & self.available_aes == 0:
            warn(
                "'guide_prism_offset' needs appropriate scales.",
                PlotnineWarning
            )
            return None

        self.aesthetic = list(set(scale.aesthetics) & self.available_aes)[0]

        info = '\n'.join([self.title, self.__class__.__name__])
        self.hash = hashlib.md5(info.encode('utf-8')).hexdigest()
        return self

    def create_geoms(self, plot):
        xaxis_position = plot.axs[0].xaxis.get_label_position()
        yaxis_position = plot.axs[0].yaxis.get_label_position()
        gca = plot.axs[0].axes

        if self.aesthetic == 'x':
            major_locs = gca.get_xticks()
            minor_locs = gca.xaxis.get_minorticklocs()
            if yaxis_position == 'left':
                offset = self.offset if major_locs[0] > minor_locs[0] else self.offset / 2
            else:
                offset = self.offset if major_locs[-1] < minor_locs[-1] else self.offset / 2
            gca.spines[yaxis_position].set_position(('outward', offset))
            gca.set_xlim(min(major_locs), max(major_locs))
        else:
            major_locs = gca.get_yticks()
            minor_locs = gca.yaxis.get_minorticklocs()
            if xaxis_position == 'bottom':
                offset = self.offset if major_locs[0] > minor_locs[0] else self.offset / 2
            else:
                offset = self.offset if major_locs[-1] < minor_locs[-1] else self.offset / 2
            gca.spines[xaxis_position].set_position(('outward', offset))
            gca.set_ylim(min(major_locs), max(major_locs))

    def merge(self, other):
        """
        Simply discards the other guide
        """
        return self

    def draw(self):
        ...

class guide_prism_offset_minor(guide_prism_offset):

    def create_geoms(self, plot):
        xaxis_position = plot.axs[0].xaxis.get_label_position()
        yaxis_position = plot.axs[0].yaxis.get_label_position()
        gca = plot.axs[0].axes

        if self.aesthetic == 'x':
            gca.spines[yaxis_position].set_position(('outward', self.offset))
            major_locs = gca.get_xticks()
            minor_locs = gca.xaxis.get_minorticklocs()
            min_loc = min(min(major_locs), min(minor_locs))
            max_loc = max(max(major_locs), max(minor_locs))
            gca.set_xlim(min_loc, max_loc)
        else:
            gca.spines[xaxis_position].set_position(('outward', self.offset))
            major_locs = gca.get_yticks()
            minor_locs = gca.yaxis.get_minorticklocs()
            min_loc = min(min(major_locs), min(minor_locs))
            max_loc = max(max(major_locs), max(minor_locs))
            gca.set_ylim(min_loc, max_loc)
