import pytest

from bstb.core import Latitude
from bstb.core import Longitude
from bstb.core import Waypoint
from bstb.greatcircle import bearing


def test_bearing_01():
    wp0 = Waypoint()
    wp0.latitude = Latitude.dms(50, 3, 59)
    wp0.longitude = Longitude.dms(-5, 42, 53)
    wp1 = Waypoint()
    wp1.latitude = Latitude.dms(58, 38, 38)
    wp1.longitude = Longitude.dms(-3, 4, 12)

    b = bearing(wp0, wp1)

    assert b.degrees == pytest.approx(9.119818)
    assert str(b) == "009.1"


def test_bearing_02():
    wp0 = Waypoint.parse("N52 00.000 E004 00.000")
    wp1 = Waypoint.parse("N51 58.000 E004 10.000")
    b = bearing(wp0, wp1)

    assert b.degrees == pytest.approx(107.92465)
    assert str(b) == "107.9"
