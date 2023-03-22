from bstb.core import Bearing
from bstb.core import Distance
from bstb.core import Latitude
from bstb.core import Longitude
from bstb.core import Waypoint

from bstb.greatcircle import destination


def test_destination_01():
    wp0 = Waypoint()
    wp0.latitude = Latitude.dms(53, 19, 14)
    wp0.longitude = Longitude.dms(-1, 43, 47)
    b = Bearing.dms(96, 1, 18)
    d = Distance(124.8)

    wp1 = destination(wp0, b, d)

    assert str(wp1) == "N53 11.290 E000 08.072"


def test_destination_02():
    wp0 = Waypoint.parse("N52 00.000 E004 00.000")
    b = Bearing(101)
    d = Distance(12.5)

    wp1 = destination(wp0, b, d)

    assert str(wp1) == "N51 58.704 E004 10.756"
