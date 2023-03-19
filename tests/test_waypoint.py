import pytest

from bstb import is_valid_waypoint, parse_waypoint, distance, bearing


def test_is_valid_waypoint():
    assert is_valid_waypoint("N51 58.789 E004 08.234")


def test_not_valid_waypoint():
    assert not is_valid_waypoint("aap noot mies")


def test_parse_waypoint_NE():
    lat, lng = parse_waypoint("N45 00.000 E090 00.000")
    assert lat == 45.0
    assert lng == 90.0


def test_parse_waypoint_SE():
    lat, lng = parse_waypoint("S45 00.000 E090 00.000")
    assert lat == -45.0
    assert lng == 90.0


def test_parse_waypoint_SW():
    lat, lng = parse_waypoint("S45 00.000 W090 00.000")
    assert lat == -45.0
    assert lng == -90.0


def test_parse_waypoint_NW():
    lat, lng = parse_waypoint("N45 00.000 W090 00.000")
    assert lat == 45.0
    assert lng == -90.0


def test_parse_waypoint_aap():
    lat, lng = parse_waypoint("aap noot mies")
    assert lat == None
    assert lng == None


def test_distance_01():
    """See: https://www.movable-type.co.uk/scripts/latlong.html"""
    latA = 50 + 3 / 60 + 59 / 3600
    lngA = -5 - 42 / 60 - 53 / 3600
    latB = 58 + 38 / 60 + 38 / 3600
    lngB = -3 - 4 / 60 - 12 / 3600

    d = distance(latA, lngA, latB, lngB)

    assert d == pytest.approx(968.853)

    b = bearing(latA, lngA, latB, lngB)

    assert b == pytest.approx(9.119818)
