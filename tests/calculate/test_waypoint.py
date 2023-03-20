
import pytest

from bstb.core import Bearing
from bstb.core import Distance
from bstb.core import Latitude
from bstb.core import Longitude
from bstb.core import Waypoint

from bstb.calculate import waypoint

def test_waypoint_01():
    a_wp = Waypoint()
    a_wp.latitude = Latitude.dms(53, 19, 14)
    a_wp.longitude = Longitude.dms(-1, 43, 47)    
    b = Bearing.dms(96, 1, 18)
    d = Distance()
    d.km = 124.8

    b_wp = waypoint(a_wp, b, d)

    assert str(b_wp) == "N53 11.290 E000 08.072"
