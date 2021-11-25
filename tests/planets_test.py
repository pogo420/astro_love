from planets import Planets
import pytest


def test_sanity():
    """Function for sanity testing of planets logic"""
    try:
        for i in Planets().get_current_planets():
            print(i)
        for i in Planets().get_planets_at_utc(2021, 11, 25, 16, 16, 0.0):
            print(i)
    except:
        pytest.fail("Issue in sanity test case of Planets logic")


def test_utc_check():
    """Function to check the utc logic"""

    planets = list(Planets().get_planets_at_utc(2021, 11, 25, 16, 16, 0.0))
    response = ["""Azimuth: 246deg 06' 11.5", Altitude: -12deg 13' 13.0", Name: venus""",
                """Azimuth: 255deg 34' 03.6", Altitude: -71deg 20' 06.4", Name: mars""",
                """Azimuth: 247deg 01' 49.7", Altitude: 25deg 29' 11.6", Name: JUPITER BARYCENTER""",
                """Azimuth: 247deg 58' 33.6", Altitude: 09deg 22' 10.7", Name: SATURN BARYCENTER""",
                ]
    assert planets == response
