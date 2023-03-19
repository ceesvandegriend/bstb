import math
import pytest

from bstb.core import Longitude


def test_consructor_01():
    lng = Longitude()

    assert lng.degrees == 0
    assert lng.radians == 0


def test_consructor_02():
    lng = Longitude(45.25)

    assert lng.degrees == 45.25
    assert lng.radians == pytest.approx(math.radians(45.25))


def test_consructor_03():
    with pytest.raises(ValueError):
        Longitude(-180.25)


def test_consructor_04():
    with pytest.raises(ValueError):
        Longitude(180.25)


def test_str_01():
    lng = Longitude(0)

    assert str(lng) == "E000 00.000"


def test_str_02():
    lng = Longitude(45.25)

    assert str(lng) == "E045 15.000"


def test_str_03():
    lng = Longitude(-45.25)

    assert str(lng) == "W045 15.000"


def test_dm_01():
    lng = Longitude.dm(45, 15.0)

    assert str(lng) == "E045 15.000"


def test_dm_02():
    lng = Longitude.dm(-45, 15.0)

    assert str(lng) == "W045 15.000"


def test_dms_01():
    lng = Longitude.dms(45, 15, 15)

    assert str(lng) == "E045 15.250"


def test_dms_02():
    lng = Longitude.dms(-45, 15, 15)

    assert str(lng) == "W045 15.250"
