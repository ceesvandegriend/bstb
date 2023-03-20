import pytest

from bstb.core import Latitude
from bstb.core import Longitude
from bstb.core import Waypoint
from bstb.calculate import bearing


def test_distance_01():
    """See: https://www.movable-type.co.uk/scripts/latlong.html"""

    a_wp = Waypoint()
    a_wp.latitude = Latitude.dms(50, 3, 59)
    a_wp.longitude = Longitude.dms(-5, 42, 53)
    b_wp = Waypoint()
    b_wp.latitude = Latitude.dms(58, 38, 38)
    b_wp.longitude = Longitude.dms(-3, 4, 12)

    b = bearing(a_wp, b_wp)

    assert b.degrees == pytest.approx(9.119818)
    assert str(b) == "009.1"
