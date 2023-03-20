import pytest

from bstb.core import Latitude
from bstb.core import Longitude
from bstb.core import Waypoint
from bstb.calculate import bearing


def test_distance_01():
    """See: https://www.movable-type.co.uk/scripts/latlong.html"""

    a_lat = Latitude.dms(50, 3, 59)
    a_lng = Longitude.dms(-5, 42, 53)
    b_lat = Latitude.dms(58, 38, 38)
    b_lng = Longitude.dms(-3, 4, 12)
    a_wp = Waypoint(a_lat, a_lng)
    b_wp = Waypoint(b_lat, b_lng)

    b = bearing(a_wp, b_wp)

    assert b.degrees == pytest.approx(9.119818)
    assert str(b) == "009.120"
