from functools import lru_cache
from pathlib import Path

import toml
from diot import Diot

SCHEMES_DIR = Path(__file__).parent.joinpath('schemes')

@lru_cache()
def list_themes():
    return [
        tfile.stem
        for tfile in SCHEMES_DIR.glob("*.toml")
        if not tfile.stem.startswith('_')
    ]

@lru_cache()
def _all_color_pals():
    with SCHEMES_DIR.joinpath('_color_palettes.toml').open() as fcolor:
        return toml.load(fcolor)

@lru_cache()
def _all_fill_pals():
    with SCHEMES_DIR.joinpath('_fill_palettes.toml').open() as ffill:
        return toml.load(ffill)

@lru_cache()
def _all_shape_pals():
    with SCHEMES_DIR.joinpath('_shape_palettes.toml').open() as fshape:
        return toml.load(fshape)

@lru_cache()
def theme_colors(palette):
    with SCHEMES_DIR.joinpath(f"{palette}.toml") as fsch:
        return Diot(toml.load(fsch))

def list_color_pals():
    return list(_all_color_pals())

def list_fill_pals():
    return list(_all_fill_pals())

def list_shape_pals():
    return list(_all_shape_pals())

def prism_color_pal(palette):
    return lambda n: _all_color_pals()[palette][:n]

def prism_fill_pal(palette):
    return lambda n: _all_fill_pals()[palette][:n]

def prism_shape_pal(palette):
    return lambda n: _all_shape_pals()[palette][:n]
