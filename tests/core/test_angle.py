import math
import pytest

from bstb.core import Angle


def test_consructor_01():
    a = Angle()

    assert a.degrees == 0
    assert a.radians == 0


def test_consructor_02():
    a = Angle(45.25)

    assert a.degrees == 45.25
    assert a.radians == pytest.approx(math.radians(45.25))


def test_valid_01():
    a = Angle()

    assert not a.valid(-361)
    assert a.valid(-360)
    assert a.valid(0)
    assert a.valid(360)
    assert not a.valid(361)
