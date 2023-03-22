import pytest

from bstb.core import Latitude
from bstb.core import Longitude
from bstb.core import Waypoint
from bstb.greatcircle import distance


def test_distance_01():
    wp0 = Waypoint()
    wp0.latitude = Latitude.dms(50, 3, 59)
    wp0.longitude = Longitude.dms(-5, 42, 53)
    wp1 = Waypoint()
    wp1.latitude = Latitude.dms(58, 38, 38)
    wp1.longitude = Longitude.dms(-3, 4, 12)

    d = distance(wp0, wp1)

    assert str(d) == "968.854"
    assert d.degrees == pytest.approx(968.853 / (1.852 * 60))


def test_distance_02():
    wp0 = Waypoint.parse("N52 00.000 E004 00.000")
    wp1 = Waypoint.parse("N51 58.000 E004 10.000")
    d = distance(wp0, wp1)

    assert d.km == pytest.approx(12.000713)
    assert str(d) == "12.001"
