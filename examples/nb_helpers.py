"""Helpers for notebooks"""

import numpy
from plotnine.options import set_option
from IPython.display import display
from ipywidgets import widgets
from datar import options
options(import_names_conflict="silent")
from datar.all import f, as_categorical, mutate, complete_cases, filter, tibble
from datar.datasets import ToothGrowth, msleep, mtcars

from scipy.optimize import curve_fit#, differential_evolution

ToothGrowth >>= mutate(
    dose=as_categorical(f.dose),
    supp=as_categorical(f.supp),
)

msleep = (
    msleep >> filter(complete_cases(f)) >> mutate(vore=as_categorical(f.vore))
)

mtcars >>= mutate(cyl=as_categorical(f.cyl))

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


# function for genetic algorithm to minimize (sum of squared error)
# def sumsq_error(params, x, y):
#     warnings.filterwarnings("ignore") # do not print warnings by genetic algorithm
#     val = formula(x, *params)
#     return numpy.sum((y - val) ** 2.0)


# def initiate_params(x, y):
#     # min and max used for bounds
#     max_x = max(x)
#     min_x = min(x)
#     max_y = max(y)
#     # minY = min(y)

#     param_bounds = []
#     param_bounds.append([min_x, max_x]) # search bounds for a
#     param_bounds.append([min_x, max_x]) # search bounds for b
#     param_bounds.append([0.0, max_y]) # search bounds for Offset

#     # "seed" the numpy random number generator for repeatable results
#     result = differential_evolution(
#         functools.partial(sumsq_error, x=x, y=y),
#         param_bounds,
#         seed=3
#     )
#     return result.x


def nls_formula(xseq, minv, maxv, ec50, hill_coeff):
    return minv + (
        (maxv - minv) / (1 + numpy.exp(hill_coeff * (ec50 - numpy.array(xseq))))
    )


def nls(data, xseq, **params):
    # * data - has the x and y values for the model
    # * xseq - x values to be predicted
    # * params - stat parameters
    #
    # It must return a new dataframe. Below is the
    # template used internally by Plotnine

    # Input data into the model
    x, y = data["x"], data["y"]

    params = params['method_args']

    # init_params = initiate_params(x, y)
    # fitted_params, _ = curve_fit(nls_formula, x, y, init_params)
    fitted_params, _ = curve_fit(
        nls_formula,
        x,
        y,
        (params["minv"], params["maxv"], params["ec50"], params["hill_coeff"]),
    )

    # Create and fit a model
    # model = Model(x, y)
    # results = Model.fit()
    predicted = nls_formula(xseq, *fitted_params)

    # Create output data by getting predictions on
    # the xseq values
    return tibble(x=xseq, y=predicted)
