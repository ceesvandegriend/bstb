import pytest

from bstb.core import Latitude
from bstb.core import Longitude
from bstb.core import Waypoint

from bstb.loxodrome import bearing


def test_bearing_01():
    """See: https://www.movable-type.co.uk/scripts/latlong.html"""
    wp0 = Waypoint()
    wp0.latitude = Latitude.dms(50, 21, 59)
    wp0.longitude = Longitude.dms(-4, 8, 2)
    wp1 = Waypoint()
    wp1.latitude = Latitude.dms(42, 21, 4)
    wp1.longitude = Longitude.dms(-71, 2, 27)

    b = bearing(wp0, wp1)

    assert b.degrees == pytest.approx(260.12718)
    assert str(b) == "260.1"


# def test_bearing_02():
#     wp0 = Waypoint.parse("N52 00.000 E004 00.000")
#     wp1 = Waypoint.parse("N51 58.000 E004 10.000")
#     b = bearing(wp0, wp1)

#     assert b.degrees == 107.9
#     assert str(b) == "107.9"
