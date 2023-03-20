"""
Great-circle calculations are used.

See: https://www.movable-type.co.uk/scripts/latlong.html
"""
import math

from bstb.core import Bearing
from bstb.core import Distance
from bstb.core import Waypoint


def bearing(a: Waypoint, b: Waypoint) -> Bearing:
    """Calculate the initial bearing in degrees between 2 waypoints."""
    delta_lng = b.longitude.radians - a.longitude.radians
    a_lat = a.latitude.radians
    b_lat = b.latitude.radians

    y = math.sin(delta_lng) * math.cos(b_lat)
    x = math.cos(a_lat) * math.sin(b_lat) - math.sin(a_lat) * math.cos(b_lat) * math.cos(delta_lng)
    z = math.atan2(y, x)
    b = Bearing()
    b.degrees = (math.degrees(z) + 360) % 360

    return b


def distance(a: Waypoint, b: Waypoint) -> Distance:
    """Calculate the distance in km between 2 waypoints."""
    R = 6_371  # R earth in km
    delta_lat = b.latitude.radians - a.latitude.radians
    delta_lng = b.longitude.radians - a.longitude.radians
    a_lat = a.latitude.radians
    b_lat = b.latitude.radians

    # Haversine formula
    a = math.sin(delta_lat / 2) * math.sin(delta_lat / 2) + math.cos(a_lat) * math.cos(b_lat) * math.sin(
        delta_lng / 2
    ) * math.sin(delta_lng / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = Distance(c * R)

    return d


def destination(a_wp: Waypoint, bear: Bearing, dist: Distance) -> Waypoint:
    """Given a start waypoint, initial bearing and distance, calculate the new waypoint.

    See: https://www.movable-type.co.uk/scripts/latlong.html
    """
    a_lat = a_wp.latitude.radians
    a_lng = a_wp.longitude.radians
    b = bear.radians
    d = dist.radians

    b_lat = math.asin(math.sin(a_lat) * math.cos(d) + math.cos(a_lat) * math.sin(d) * math.cos(b))
    delta_lng = math.atan2(
        math.sin(b) * math.sin(d) * math.cos(a_lat), math.cos(d) - math.sin(a_lat) * math.sin(b_lat)
    )
    b_lng = a_lng + delta_lng

    b_wp = Waypoint()
    b_wp.latitude.radians = b_lat
    b_wp.longitude.radians = b_lng

    return b_wp
