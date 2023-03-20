import math
import pytest

from bstb.core import Distance


def test_constructor_01():
    d = Distance()

    assert d.degrees == 0


def test_valid_01():
    d = Distance()

    assert not d.valid(-1)
    assert d.valid(0)
    assert d.valid(1)
    assert d.valid(90)
    assert d.valid(180)
    assert not d.valid(181)


def test_km_02():
    d = Distance()
    d.km = 1.852 * 60

    assert d.degrees == 1


def test_str_01():
    d = Distance()

    assert str(d) == "0.000"


def test_str_02():
    d = Distance(100 / (1.852 * 60))

    assert str(d) == "100.000"

def test_01():
    d = Distance(45)

    assert d.degrees == 45

def test_02():
    nm = 60
    deg = nm / 60

    d = Distance(deg)

    assert d.degrees == 1


def test_03():
    km = 100
    deg = km / (60 * 1.852)

    d = Distance(deg)

    assert str(d) == "100.000"

def test_04():
    rad = math.pi / 2
    deg = math.degrees(rad)

    d = Distance(deg)

    assert d.degrees == pytest.approx(90.0)

