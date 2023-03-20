import math

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


def test_01():
    d = Distance(45)

    assert d.degrees == 45
    assert d.radians == math.pi / 4
    assert d.nm == 45 * 60
    assert d.km == 45 * 60 * 1.852
    assert str(d) == f"{45 * 60 * 1.852:0.3f}"


def test_02():
    d = Distance()
    d.nm = 60

    assert d.degrees == 1
    assert d.radians == math.pi / 180
    assert d.nm == 60
    assert d.km == 60 * 1.852
    assert str(d) == f"{60 * 1.852:0.3f}"


def test_03():
    d = Distance()
    d.km = 100

    assert d.degrees == 100 / (60 * 1.852)
    assert d.radians == 100 * (math.pi / 180) / (60 * 1.852)
    assert d.nm == 100 / 1.852
    assert d.km == 100
    assert str(d) == "100.000"
