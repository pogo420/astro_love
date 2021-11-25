from skyfield.api import load, Topos


class Planet:
    """Class to manage Planet"""

    def __init__(self, right_ascension: str, declination: str, azimuth: str, altitude: str, name: str):
        self.__right_ascension = right_ascension
        self.__declination = declination
        self.__azimuth = azimuth
        self.__altitude = altitude
        self.__name = name

    def get_current_location(self) -> str:
        return f"Azimuth: {self.__azimuth}, Altitude: {self.__altitude}, Name: {self.__name}"


class Planets:
    """Class to manage planets"""

    def __init__(self):
        self.__planet_raw = load('de421.bsp')
        self.__visible_planets = ["venus", "mars", "JUPITER BARYCENTER", "SATURN BARYCENTER"]
        self.__source_planet = "earth"
        self.__longitude = "12.9716 N"
        self.__latitude = "77.5946 E"
        self.__ts = load.timescale()
        self.__current_time = self.__ts.now()

    def __get_source(self):
        """Returning the source planet"""
        return self.__planet_raw[self.__source_planet]

    def __get_latlong(self):
        """Generating latitude longitude access"""
        return Topos(self.__longitude, self.__latitude)

    def __get_current_location(self, source):
        """Generating current location"""
        return source + Topos(self.__longitude, self.__latitude)

    def __generate_timestamp(self, year, month, day, hour, minute, second):
        return self.__ts.utc(year, month, day, hour, minute, second)

    def __generate_planet_list(self, datetime=None):
        """method implementing planet list logic"""
        source_planet = self.__get_source()
        current_location = self.__get_current_location(source_planet)

        datetime = self.__current_time if datetime is None else datetime

        for planet in self.__visible_planets:
            astrometric = current_location.at(datetime).observe(self.__planet_raw[planet])

            right_ascension, declination, distance = astrometric.radec()
            altitude, azimuth, distance_ = astrometric.apparent().altaz()

            yield Planet(right_ascension, declination, azimuth, altitude, planet).get_current_location()

    def get_planets_at_utc(self, year, month, day, hour, minute, second):
        """Method to get planet locations as per utc time"""
        datetime = self.__generate_timestamp(year, month, day, hour, minute, second)
        return self.__generate_planet_list(datetime)

    def get_current_planets(self):
        """Method to get current planet locations"""
        return self.__generate_planet_list()

