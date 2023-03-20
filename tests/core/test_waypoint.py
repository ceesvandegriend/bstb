import pytest

from bstb.core import Waypoint


def test_constructor_01():
    wp = Waypoint()

    assert wp
    assert wp.latitude
    assert wp.latitude.degrees == 0
    assert wp.latitude.radians == 0
    assert wp.longitude
    assert wp.longitude.degrees == 0
    assert wp.longitude.radians == 0


def test_parse_01():
    wp = Waypoint.parse("N52 00.000 E004 00.000")

    assert wp
    assert wp.latitude
    assert wp.latitude.degrees == 52
    assert wp.longitude
    assert wp.longitude.degrees == 4

    assert str(wp) == "N52 00.000 E004 00.000"


def test_parse_02():
    with pytest.raises(ValueError):
        Waypoint.parse("aap noot mies")
