import re

__REGEX = r"^[NnSs][0123456789]{1,2}.[0123456789]{1,2}\.[0123456789]{1,3}.[EeWw][0123456789]{1,3}.[0123456789]{1,2}\.[0123456789]{1,3}$"


def is_valid_waypoint(waypoint: str) -> bool:
    """Checks if the string is a valid coordinate."""
    result = re.match(__REGEX, waypoint)

    if result:
        return True
    else:
        return False
