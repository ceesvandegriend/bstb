# Usage

## Calculate bearing

Given 2 locations, calculate the bearing in degrees (0 .. 360).

```python
from bstb.core import Waypoint
from bstb.greatcircle import bearing

wp0 = Waypoint.parse("N52 00.000 E004 00.000")
wp1 = Waypoint.parse("N51 58.000 E004 10.000")
b = bearing(wp0, wp1)

print(f"Bearing: {b}") # 107.9
```

## Calculate distance

Given 2 locations, calculate the distance in km.

```python
from bstb.core import Waypoint
from bstb.greatcircle import distance

wp0 = Waypoint.parse("N52 00.000 E004 00.000")
wp1 = Waypoint.parse("N51 58.000 E004 10.000")
d = distance(wp0, wp1)

print(f"Distance: {d} km") # 12.001
```

## Calculate destination

Given a start location, a bearing and distance in km,
calculate the final location.

```python
from bstb.core import Bearing
from bstb.core import Distance
from bstb.core import Waypoint
from bstb.greatcircle import destination

wp0 = Waypoint.parse("N52 00.000 E004 00.000")
b = Bearing(101)
d = Distance(12.5)
wp1 = destination(wp0, b, d)

print(f"Destination: {wp1}") # N51 58.704 E004 10.756
```

## More examples

Look in the `tests/` directory for more examples.
