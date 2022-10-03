#!/bin/env python3

"""Scratchpad"""

import datetime
import json
import requests
from constants import constant1, constant2

# test lat/lon values:  47.6987, -117.4397 (also, elevation is 526 m)
#def get_sun_position(latitude, longitude):
def get_sun_position():

    """ Returns the current position of the Sun in the sky at
        the specified location.

        Parameters:
        latitude (str)
        longitude (str)
        
        Returns:
        float:  altitude
        float:  azimuth
    """

    astronomy_api = ("https://api.astronomyapi.com/api/v2/bodies/positions/sun")
    let_me_in = (constant1, constant2)
    values = {  "latitude": str(47.6987),
                "longitude": str(-117.4397),
                "elevation": str(526), # in meters
                "from_date": str('2017-12-20'),
                "time": "08:00:00",
                "to_date": str('2017-12-20')}
    response = requests.get(astronomy_api, auth=let_me_in, params=values)
    response_data = json.loads(response.content)
    position = response_data["data"]["table"]["rows"][0]["cells"][0]["position"]["horizontal"]
    altitude = position["altitude"]["degrees"]
    azimuth = position["azimuth"]["degrees"]
    print(f'The Sun is currently at altitude {altitude} and azimuth {azimuth}.')
    return azimuth, altitude

get_sun_position()

# get_sun_position is working with test values.  Need to refine.

#######################################################################

# def get_location():
#     """ Returns the longitude and latitude for the location of an IP.

#         Returns:
#         float:  latitude
#         float:  longitude
#         """
#     target = requests.get('http://ip-api.com/json/174.31.14.127?fields=lat,lon')
#     target_data = json.loads(target.text)
#     latitude = (target_data['lat'])
#     longitude = (target_data['lon'])
#     return latitude, longitude

# get_location()

#get_location is now working and returns the desired values.  Copied into solar.py
