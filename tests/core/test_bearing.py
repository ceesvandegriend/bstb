from bstb.core import Bearing


def test_constructor_01():
    b = Bearing(0)

    assert b.degrees == 0


def test_valid_01():
    b = Bearing(0)

    assert not b.valid(-1)
    assert b.valid(0)
    assert b.valid(90)
    assert b.valid(180)
    assert b.valid(270)
    assert not b.valid(360)
    assert not b.valid(361)


def test_str_01():
    n = Bearing(0)
    e = Bearing(90)
    s = Bearing(180)
    w = Bearing(270)

    assert str(n) == "000.0"
    assert str(e) == "090.0"
    assert str(s) == "180.0"
    assert str(w) == "270.0"
