[![CI](https://github.com/ceesvandegriend/bstb/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/ceesvandegriend/bstb/actions/workflows/ci.yml)

[Geocaching](https://www.geocaching.com/) toolbox as a Python package on
[PyPi](https://www.pypi.org/project/bstb/).

## Documentation

Documentation for
[`bstb`](https://bstb.griend.eu/)
is available.

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
