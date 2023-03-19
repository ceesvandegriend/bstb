import math
import pytest

from bstb.core import Latitude


def test_consructor_01():
    lat = Latitude()

    assert lat.degrees == 0
    assert lat.radians == 0


def test_consructor_02():
    lat = Latitude(45.25)

    assert lat.degrees == 45.25
    assert lat.radians == pytest.approx(math.radians(45.25))


def test_consructor_03():
    with pytest.raises(ValueError):
        Latitude(-90.25)


def test_consructor_04():
    with pytest.raises(ValueError):
        Latitude(90.25)


def test_str_01():
    lat = Latitude(0)

    assert str(lat) == "N00 00.000"


def test_str_02():
    lat = Latitude(45.25)

    assert str(lat) == "N45 15.000"


def test_str_03():
    lat = Latitude(-45.25)

    assert str(lat) == "S45 15.000"


def test_dm_01():
    lat = Latitude.dm(45, 15.0)

    assert str(lat) == "N45 15.000"


def test_dm_02():
    lat = Latitude.dm(-45, 15.0)

    assert str(lat) == "S45 15.000"


def test_dms_01():
    lat = Latitude.dms(45, 15, 15)

    assert str(lat) == "N45 15.250"


def test_dms_02():
    lat = Latitude.dms(-45, 15, 15)

    assert str(lat) == "S45 15.250"
