"""Provides available palettes"""

from functools import lru_cache
from pathlib import Path

import rtoml
from diot import Diot

SCHEMES_DIR = Path(__file__).parent.joinpath("schemes")


@lru_cache()
def list_themes():
    """List all available theme palettes"""
    return [
        tfile.stem
        for tfile in SCHEMES_DIR.glob("*.toml")
        if not tfile.stem.startswith("_")
    ]


@lru_cache()
def _all_color_pals():
    with SCHEMES_DIR.joinpath("_color_palettes.toml").open() as fcolor:
        return rtoml.load(fcolor)


@lru_cache()
def _all_fill_pals():
    with SCHEMES_DIR.joinpath("_fill_palettes.toml").open() as ffill:
        return rtoml.load(ffill)


@lru_cache()
def _all_shape_pals():
    with SCHEMES_DIR.joinpath("_shape_palettes.toml").open() as fshape:
        return rtoml.load(fshape)


@lru_cache()
def theme_colors(palette):
    """Get the colors for a specific theme"""
    with SCHEMES_DIR.joinpath(f"{palette}.toml").open() as fsch:
        return Diot(rtoml.load(fsch))


def list_color_pals():
    """List all available color palettes"""
    return list(_all_color_pals())


def list_fill_pals():
    """List all available fill palettes"""
    return list(_all_fill_pals())


def list_shape_pals():
    """List all available shape palettes"""
    return list(_all_shape_pals())


def prism_color_pal(palette):
    """Get the prism color palette by name"""
    return lambda n: _all_color_pals()[palette][:n]


def prism_fill_pal(palette):
    """Get the prism fill palette by name"""
    return lambda n: _all_fill_pals()[palette][:n]


def prism_shape_pal(palette):
    """Get the prism shape palette by name"""
    return lambda n: _all_shape_pals()[palette][:n]


list_colour_pals = list_color_pals
prism_colour_pal = prism_color_pal
