# Usage: Bearing

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
