import math
import re

__REGEX = r"^([NnSs])([0123456789]{1,2}).([0123456789]{1,2}\.[0123456789]{1,3}).([EeWw])([0123456789]{1,3}).([0123456789]{1,2}\.[0123456789]{1,3})$"


def is_valid_waypoint(waypoint: str) -> bool:
    """Checks if the string is a valid coordinate."""
    result = re.match(__REGEX, waypoint)

    if result:
        return True
    else:
        return False


def parse_waypoint(waypoint: str):
    """Returns the latitude and longitude in degrees."""
    result = re.match(__REGEX, waypoint)

    if result:
        lat_sign = -1 if result.group(1) in "Ss" else 1
        lat_deg = int(result.group(2))
        lat_min = float(result.group(3))
        lng_sign = -1 if result.group(4) in "Ww" else 1
        lng_deg = int(result.group(5))
        lng_min = float(result.group(6))

        lat = lat_sign * (lat_deg + (lat_min / 60))
        lng = lng_sign * (lng_deg + (lng_min / 60))

        return lat, lng
    else:
        return None, None


def distance(latA: float, lngA: float, latB: float, lngB: float) -> float:
    """Calculate the distance in km between 2 waypoints.

    See: https://www.movable-type.co.uk/scripts/latlong.html
    """
    R = 6_371  # R earth in m
    delta_lat = math.radians(latB - latA)
    delta_lng = math.radians(lngB - lngA)
    latA = math.radians(latA)
    # lngA = math.radians(lngA)
    latB = math.radians(latB)
    # lngB = math.radians(lngB)

    # Haversine formula
    a = math.sin(delta_lat / 2) * math.sin(delta_lat / 2) + math.cos(latA) * math.cos(latB) * math.sin(
        delta_lng / 2
    ) * math.sin(delta_lng / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = c * R
    return d


def bearing(latA: float, lngA: float, latB: float, lngB: float) -> float:
    """Calculate the initial bearing in degrees between 2 waypoints.

    See: https://www.movable-type.co.uk/scripts/latlong.html
    """
    # delta_lat = math.radians(latB - latA)
    delta_lng = math.radians(lngB - lngA)
    latA = math.radians(latA)
    lngA = math.radians(lngA)
    latB = math.radians(latB)
    lngB = math.radians(lngB)

    y = math.sin(delta_lng) * math.cos(latB)
    x = math.cos(latA) * math.sin(latB) - math.sin(latA) * math.cos(latB) * math.cos(delta_lng)
    z = math.atan2(y, x)
    b = (math.degrees(z) + 360) % 360
    return b
