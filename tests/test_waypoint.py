from bstb import is_valid_waypoint


def test_is_valid_waypoint():
    assert is_valid_waypoint("N51 58.789 E004 08.234")


def test_not_valid_waypoint():
    assert not is_valid_waypoint("aap noot mies")
