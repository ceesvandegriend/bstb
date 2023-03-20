import pytest

from bstb.core import Latitude
from bstb.core import Longitude
from bstb.core import Waypoint
from bstb.calculate import distance


def test_distance_01():
    """See: https://www.movable-type.co.uk/scripts/latlong.html"""
    a_lat = Latitude.dms(50, 3, 59)
    a_lng = Longitude.dms(-5, 42, 53)
    a_wp = Waypoint(a_lat, a_lng)
    b_lat = Latitude.dms(58, 38, 38)
    b_lng = Longitude.dms(-3, 4, 12)
    b_wp = Waypoint(b_lat, b_lng)

    d = distance(a_wp, b_wp)

    assert d.km == pytest.approx(968.854)
    assert str(d) == "968.854"
    assert d.degrees == pytest.approx(968.853 / (1.852 * 60))
