from bstb.core import Bearing
from bstb.core import Distance
from bstb.core import Latitude
from bstb.core import Longitude
from bstb.core import Waypoint

from bstb.loxodrome import destination


def test_destination_01():
    wp0 = Waypoint()
    wp0.latitude = Latitude.dms(51, 7, 32)
    wp0.longitude = Longitude.dms(1, 20, 17)
    b = Bearing.dms(116, 38, 10)
    d = Distance(40.23)

    wp1 = destination(wp0, b, d)

    assert str(wp1) == "N50 57.795 E001 51.167"
