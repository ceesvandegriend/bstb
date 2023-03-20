import pytest

from bstb.core import Latitude
from bstb.core import Longitude
from bstb.core import Waypoint

from bstb.loxodrome import distance


def test_distance_01():
    wp0 = Waypoint()
    wp0.latitude = Latitude.dms(50, 21, 59)
    wp0.longitude = Longitude.dms(-4, 8, 2)
    wp1 = Waypoint()
    wp1.latitude = Latitude.dms(42, 21, 4)
    wp1.longitude = Longitude.dms(-71, 2, 27)

    d = distance(wp0, wp1)

    assert d.km == pytest.approx(5198.002)
    assert str(d) == "5198.002"
