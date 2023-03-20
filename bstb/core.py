import math
import re


class Angle:
    """Base clase, an angle in degrees."""

    def __init__(self, degrees: float = 0):
        """Construct a new angle."""
        self.degrees = degrees

    @property
    def degrees(self) -> float:
        """Returns the angle in degrees."""
        return self._degrees

    @degrees.setter
    def degrees(self, degrees: float):
        """Sets the angle in degrees."""
        if not self.valid(degrees):
            raise ValueError(degrees)
        self._degrees = degrees

    @property
    def radians(self) -> float:
        """Returns the angle in radians."""
        return math.radians(self.degrees)

    @radians.setter
    def radians(self, radians: float):
        """Sets the angle in radians."""
        self.degrees = math.degrees(radians)

    def valid(self, degrees: float) -> bool:
        """Checks if the value is valid."""
        if degrees >= -360 and degrees <= 360:
            return True
        else:
            return False


class Latitude(Angle):
    """A latitude in degrees North (positive) or Soutn (negative)."""

    def valid(self, degrees: float) -> bool:
        """Checks if the latitude is valid."""
        if degrees >= -90 and degrees <= 90:
            return True
        else:
            return False

    def __str__(self):
        """Returns the latitude formatted as a string."""
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
        """ "Creates a new latitude with the given degrees and minutes.

        If the degrees are smaller then 0, it is a South latitude, else
        a North latitude.
        """
        if degrees < 0:
            lat = degrees - (minutes / 60)
        else:
            lat = degrees + (minutes / 60)
        return Latitude(lat)

    @classmethod
    def dms(cls, degrees: int, minutes: int, seconds: int):
        """ "Creates a new latitude with the given degrees, minutes and seconds.

        If the degrees are smaller then 0, it is a South latitude, else
        a North latitude.
        """
        if degrees < 0:
            lat = degrees - (minutes / 60) - (seconds / 3600)
        else:
            lat = degrees + (minutes / 60) + (seconds / 3600)
        return Latitude(lat)


class Longitude(Angle):
    """A longitude in degrees East (positive) or West (negative)."""

    def valid(self, degrees: float) -> bool:
        """Checks if the longitude is valid."""
        if degrees >= -180 and degrees <= 180:
            return True
        else:
            return False

    def __str__(self):
        """Returns the longitude formatted as a string."""
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
        """ "Creates a new longitude with the given degrees and minutes.

        If the degrees are smaller then 0, it is a West longitude, else
        a East longitude.
        """
        if degrees < 0:
            lng = degrees - (minutes / 60)
        else:
            lng = degrees + (minutes / 60)
        return Longitude(lng)

    @classmethod
    def dms(cls, degrees: int, minutes: int, seconds: int):
        """ "Creates a new longitude with the given degrees, minutes and seconds.

        If the degrees are smaller then 0, it is a West longitude, else
        a East longitude.
        """
        if degrees < 0:
            lng = degrees - (minutes / 60) - (seconds / 3600)
        else:
            lng = degrees + (minutes / 60) + (seconds / 3600)
        return Longitude(lng)


class Bearing(Angle):
    """A bearing in degrees from 0 to 360."""

    def valid(self, degrees: float) -> bool:
        """Checks if the bearing is valid."""
        if degrees >= 0 and degrees < 360:
            return True
        else:
            return False

    def __str__(self):
        """Retsuns the bearing formatted as a string."""
        return f"{self.degrees:05.1f}"

    @classmethod
    def dms(cls, degrees: int = 0, minutes: int = 0, seconds: int = 0):
        """Creates a new bearing with the given degrees, minutes and seconds."""
        deg = degrees + (minutes / 60) + (seconds / 3600)
        return Bearing(deg)


class Distance(Angle):
    """The distance is internally stored in degrees."""

    def __init__(self, distance: float = 0):
        """Creates a new distance with the given value in km."""
        super().__init__()
        self.km = distance

    def valid(self, degrees: float) -> bool:
        """Checks if the distance is valid."""
        if degrees >= 0 and degrees <= 180:
            return True
        else:
            return False

    @property
    def nm(self):
        """Gets the distance in Nautical Miles."""
        return self.degrees * 60

    @nm.setter
    def nm(self, distance: float):
        """Sets the distance in Nautical Miles."""
        self.degrees = distance / 60

    @property
    def km(self):
        """Gets the distance in km."""
        return self.nm * 1.852

    @km.setter
    def km(self, distance: float):
        """Sets the distance in km."""
        self.nm = distance / 1.852

    def __str__(self):
        """Returns the distance formatted in km."""
        return f"{self.km:0.3f}"


class Waypoint:
    """A point with a latitude and longitude."""

    def __init__(self, lat: Latitude = None, lng: Longitude = None):
        """Creates a new waypoint.."""
        self.latitude = lat if lat else Latitude()
        self.longitude = lng if lng else Longitude()

    def __str__(self):
        """Returns the waypoint formatted as a string."""
        return f"{self.latitude} {self.longitude}"

    @classmethod
    def parse(cls, waypoint: str):
        """Returns a new waypoint by parsing the string."""
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
