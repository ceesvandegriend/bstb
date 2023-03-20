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


def test_01():
    d = Distance()
    d.degrees = 45

    assert d.degrees == pytest.approx(45)
    assert d.radians == pytest.approx(math.pi / 4)
    assert d.nm == pytest.approx(45 * 60)
    assert d.km == pytest.approx(45 * 60 * 1.852)
    assert str(d) == f"{45 * 60 * 1.852:0.3f}"


def test_02():
    d = Distance()
    d.radians = math.pi / 4

    assert d.degrees == pytest.approx(45)
    assert d.radians == pytest.approx(math.pi / 4)
    assert d.nm == pytest.approx(45 * 60)
    assert d.km == pytest.approx(45 * 60 * 1.852)
    assert str(d) == f"{45 * 60 * 1.852:0.3f}"


def test_03():
    d = Distance()
    d.nm = 60

    assert d.degrees == pytest.approx(1)
    assert d.radians == pytest.approx(math.pi / 180)
    assert d.nm == pytest.approx(60)
    assert d.km == pytest.approx(60 * 1.852)
    assert str(d) == f"{60 * 1.852:0.3f}"


def test_04():
    d = Distance()
    d.km = 1852

    assert d.degrees == pytest.approx(1000 / 60)
    assert d.radians == pytest.approx((1000 / 60) * (math.pi / 180))
    assert d.nm == pytest.approx(1000)
    assert d.km == pytest.approx(1852)
    assert str(d) == "1852.000"


def test_05():
    d = Distance(1852.0)

    assert d.degrees == pytest.approx(1000 / 60)
    assert d.radians == pytest.approx((1000 / 60) * (math.pi / 180))
    assert d.nm == pytest.approx(1000)
    assert d.km == pytest.approx(1852)
    assert str(d) == "1852.000"
