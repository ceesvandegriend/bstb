import math
import re


class Angle:
    def __init__(self, degrees: float = 0):
        self.degrees = degrees

    @property
    def degrees(self) -> float:
        return self._degrees

    @degrees.setter
    def degrees(self, degrees: float):
        if not self.valid(degrees):
            raise ValueError(degrees)
        self._degrees = degrees

    @property
    def radians(self) -> float:
        return math.radians(self.degrees)

    @radians.setter
    def radians(self, radians: float):
        self.degrees = math.degrees(radians)

    def valid(self, degrees: float) -> bool:
        if degrees >= -360 and degrees <= 360:
            return True
        else:
            return False


class Latitude(Angle):
    def valid(self, degrees: float) -> bool:
        if degrees >= -90 and degrees <= 90:
            return True
        else:
            return False

    def __str__(self):
        if self.degrees < 0:
            sign = "S"
        else:
            sign = "N"

        tmp = abs(self.degrees)
        degrees = math.floor(tmp)
        minutes = (tmp - degrees) * 60

        return f"{sign}{degrees:02d} {minutes:06.3f}"

    @classmethod
    def dm(cls, degrees: int, minutes: float):
        if degrees < 0:
            lat = degrees - (minutes / 60)
        else:
            lat = degrees + (minutes / 60)
        return Latitude(lat)

    @classmethod
    def dms(cls, degrees: int, minutes: int, seconds: int):
        if degrees < 0:
            lat = degrees - (minutes / 60) - (seconds / 3600)
        else:
            lat = degrees + (minutes / 60) + (seconds / 3600)
        return Latitude(lat)


class Longitude(Angle):
    def valid(self, degrees: float) -> bool:
        if degrees >= -180 and degrees <= 180:
            return True
        else:
            return False

    def __str__(self):
        if self.degrees < 0:
            sign = "W"
        else:
            sign = "E"

        tmp = abs(self.degrees)
        degrees = int(math.floor(tmp))
        minutes = (tmp - degrees) * 60

        return f"{sign}{degrees:03d} {minutes:06.3f}"

    @classmethod
    def dm(cls, degrees: int, minutes: float):
        if degrees < 0:
            lng = degrees - (minutes / 60)
        else:
            lng = degrees + (minutes / 60)
        return Longitude(lng)

    @classmethod
    def dms(cls, degrees: int, minutes: int, seconds: int):
        if degrees < 0:
            lng = degrees - (minutes / 60) - (seconds / 3600)
        else:
            lng = degrees + (minutes / 60) + (seconds / 3600)
        return Longitude(lng)

class Bearing(Angle):
    def valid(self, degrees: float) -> bool:
        if degrees >= 0 and degrees <= 360:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.degrees:07.3f}"

    @classmethod
    def dms(cls, degrees: int, minutes: int, seconds: int):
        deg = degrees + (minutes / 60) + (seconds / 3600)
        return Bearing(deg)

class Distance(Angle):
    def valid(self, degrees: float) -> bool:
        if degrees >= 0 and degrees <= 180:
            return True
        else:
            return False

    @property
    def km(self):
        return self.degrees * 60 * 1.852

    @km.setter
    def km(self, distance: float):
        self.degrees = distance / (60 * 1.852)

    def __str__(self):
        return f"{self.km:0.3f}"



class Waypoint:
    def __init__(self):
        self.latitude = Latitude()
        self.longitude = Longitude()

    @property
    def latitude(self) -> Latitude:
        return self._latitude

    @latitude.setter
    def latitude(self, lat: Latitude):
        self._latitude = lat

    @property
    def longitude(self) -> Longitude:
        return self._longitude

    @longitude.setter
    def longitude(self, lng: Longitude):
        self._longitude = lng

    def __str__(self):
        lat = str(self.latitude)
        lng = str(self.longitude)

        return f"{lat} {lng}"

    @classmethod
    def parse(cls, waypoint: str):
        REGEX = r"^([NnSs])([0123456789]{1,2}).([0123456789]{1,2}\.[0123456789]{1,3}).([EeWw])([0123456789]{1,3}).([0123456789]{1,2}\.[0123456789]{1,3})$"
        result = re.match(REGEX, waypoint)

        if not result:
            raise ValueError(waypoint)

        lat_sign = -1 if result.group(1) in "Ss" else 1
        lat_deg = int(result.group(2))
        lat_min = float(result.group(3))
        lng_sign = -1 if result.group(4) in "Ww" else 1
        lng_deg = int(result.group(5))
        lng_min = float(result.group(6))

        wp = Waypoint()
        wp.latitude = Latitude(lat_sign * (lat_deg + (lat_min / 60)))
        wp.longitude = Longitude(lng_sign * (lng_deg + (lng_min / 60)))

        return wp
