[![CI](https://github.com/ceesvandegriend/bstb/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/ceesvandegriend/bstb/actions/workflows/ci.yml)

# bstb - Geocaching toolbox

`bstb / breastbone` is a random generated project name and has no special meaning.

## Usage

```console
$ ipython
Python 3.11.2 (main, Feb 16 2023, 03:07:35) [Clang 14.0.0 (clang-1400.0.29.202)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.11.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from bstb.core import Waypoint
   ...: from bstb.greatcircle import bearing
   ...: from bstb.greatcircle import distance
   ...: 
   ...: wp0 = Waypoint.parse("N52 00.000 E004 00.000")
   ...: wp1 = Waypoint.parse("N51 58.000 E004 10.000")
   ...: b = bearing(wp0, wp1)
   ...: d = distance(wp0, wp1)
   ...: 
   ...: print(f"Bearing: {b}, Distance: {d} km")
   ...: 
Bearing: 107.9, Distance: 12.001 km

```

## Warning

I don't know what formulas are used on
[GeoCaching Toolbox](https://www.geocachingtoolbox.com/), but I couldn't reproduce the results.

I used the formulas on [Movable Type Scripts](https://www.movable-type.co.uk/scripts/latlong.html). Those I recognized from my studies at the Nautical Collage.
