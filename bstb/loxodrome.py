"""
Loxodrome or rhumb line calculations are used.

See: https://www.movable-type.co.uk/scripts/latlong.html
"""
import math

from bstb.core import Bearing
from bstb.core import Distance
from bstb.core import Waypoint


def bearing(a: Waypoint, b: Waypoint) -> Bearing:
    delta_lng = b.longitude.radians - a.longitude.radians
    a_lat = a.latitude.radians
    b_lat = b.latitude.radians
    delta_vb = math.log(math.tan((math.pi / 4) + (b_lat / 2)) / math.tan((math.pi / 4) + (a_lat / 2)))
    tmp = Bearing()
    tmp.degrees = (math.degrees(math.atan2(delta_lng, delta_vb)) + 360) % 360

    return tmp


def distance(a: Waypoint, b: Waypoint) -> Distance:
    R = 6371  # R earth in km
    delta_lat = b.latitude.radians - a.latitude.radians
    delta_lng = b.longitude.radians - a.longitude.radians
    a_lat = a.latitude.radians
    b_lat = b.latitude.radians
    delta_vb = math.log(math.tan((math.pi / 4) + (b_lat / 2)) / math.tan((math.pi / 4) + (a_lat / 2)))
    q = delta_lat / delta_vb
    d = math.sqrt((delta_lat * delta_lat) + (q * q * delta_lng * delta_lng)) * R
    tmp = Distance(d)

    return tmp


def destination(a_wp: Waypoint, bear: Bearing, dist: Distance) -> Waypoint:
    """Given a start waypoint, initial bearing and distance, calculate the new waypoint"""
    a_lat = a_wp.latitude.radians
    a_lng = a_wp.longitude.radians
    b = bear.radians
    d = dist.radians

    delta_lat = d * math.cos(b)
    b_lat = a_lat + delta_lat
    delta_vb = math.log(math.tan((math.pi / 4) + (b_lat / 2)) / math.tan((math.pi / 4) + (a_lat / 2)))
    q = delta_lat / delta_vb
    delta_lng = d * math.sin(b) / q
    b_lng = a_lng + delta_lng

    tmp = Waypoint()
    tmp.latitude.radians = b_lat
    tmp.longitude.radians = b_lng

    return tmp
