# Usage: Destination

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
