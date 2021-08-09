from plotnine.options import set_option
from IPython.display import display
from ipywidgets import widgets
from datar.all import _no_warn
from datar.all import f, as_categorical, mutate, complete_cases, filter
from datar.datasets import ToothGrowth, msleep

ToothGrowth >>= mutate(
    dose=as_categorical(f.dose),
    supp=as_categorical(f.supp),
)

msleep = (
    msleep >> filter(complete_cases(f)) >> mutate(vore=as_categorical(f.vore))
)

set_option("figure_size", (4, 4))


def plot_grid(*plots, ncol=2):
    hboxes = []
    hbplots = []
    for plot in plots:
        out = widgets.Output()
        with out:
            display(plot)
        if len(hbplots) < ncol:
            hbplots.append(out)
        else:
            hboxes.append(widgets.HBox(hbplots))
            hbplots = [out]
    if hbplots:
        hboxes.append(widgets.HBox(hbplots))

    display(widgets.VBox(hboxes))
