#!/usr/bin/env python3
import requests
import datetime
from constants import constant1, constant2

today = datetime.date.today()
time = datetime.datetime.now()
current_time = time.strftime("%H:%M:%S")


def get_observer_location():
    """Returns the longitude and latitude for the location of this machine."""
    response = requests.get("http://ip-api.com/json/174.31.14.127?fields=lat,lon")
    data = response.json()
    latitude = data["lat"]
    longitude = data["lon"]
    return latitude, longitude


def get_observer_elevation(latitude, longitude):
    """Returns the elevation for the location of this machine."""
    response = requests.get(
        f"https://api.open-elevation.com/api/v1/lookup?locations={latitude},{longitude}"
    )
    data = response.json()
    elevation = data["results"][0]["elevation"]
    return elevation


def get_sun_position(latitude, longitude, elevation):
    """Returns the current position of the sun in the sky at the specified location"""
    params = {
        "longitude": longitude,
        "latitude": latitude,
        "elevation": elevation,
        "from_date": today,
        "to_date": today,
        "time": current_time,
    }
    response = requests.get(
        "https://api.astronomyapi.com/api/v2/bodies/positions/sun/",
        auth=(constant1, constant2),
        params=params,
    )
    data = response.json()
    altitude = data["data"]["table"]["rows"][0]["cells"][0]["position"]["horizontal"][
        "altitude"
    ]["degrees"]
    azimuth = data["data"]["table"]["rows"][0]["cells"][0]["position"]["horizontal"][
        "azimuth"
    ]["degrees"]
    return azimuth, altitude


def print_position(azimuth, altitude):
    """Prints the position of the sun in the sky using the supplied coordinates"""

    print(
        "The Sun is currently at:",
        azimuth,
        "degrees azimuth,",
        altitude,
        "degrees altitude",
    )


if __name__ == "__main__":
    latitude, longitude = get_observer_location()
    elevation = get_observer_elevation(latitude, longitude)
    azimuth, altitude = get_sun_position(latitude, longitude, elevation)
    print_position(azimuth, altitude)
