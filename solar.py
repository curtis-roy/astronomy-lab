#!/bin/env python3

""" Get the sun's position in the sky using coordinates from the API at
    https://astronomyapi.com and geolocation from <other site>.
    'Always know where your towel is.'  --Ford Prefect
    """

import datetime
import requests
from constants import constant1, constant2
import json

eochair = constant1
runda = constant2

def get_location():
    """ Returns the longitude and latitude for the location of an IP.

        Returns:
        float:  latitude
        float:  longitude
        """
    target = requests.get('http://ip-api.com/json/174.31.14.127?fields=lat,lon')
    target_data = json.loads(target.text)
    latitude = (target_data['lat'])
    longitude = (target_data['lon'])
    return latitude, longitude

get_location()

###############################
####  PICK IT BACK UP HERE ####
###############################

# def get_sun_position(latitude, longitude):
#     """Returns the current position of the sun in the sky at the specified location.

#     Parameters:
#     latitude (str)
#     longitude (str)

#     Returns:
#     float: azimuth
#     float: altitude
#     """

#     # add return values here when available
#     return 0, 0

# def print_position(azimuth, altitude):
#     """Prints the position of the sun in the sky using the supplied coordinates
    
#     Parameters:
#     azimuth (float)
#     altitude (float)
#     """

#     print('The Sun is currently at: ')

# if __name__ == "__main__":
#     latitude, longitude = get_location()
#     azimuth, altitude = get_sun_position()
#     print_position(azimuth, altitude)


