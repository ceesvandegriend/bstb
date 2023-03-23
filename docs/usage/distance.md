# Usage: Distance

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
