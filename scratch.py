#!/bin/env python3

"""Scratchpad"""

import datetime
import json
import requests
from constants import constant1, constant2

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
    return latitude,longitude

get_location()

# test lat/lon values:  47.6987, -117.4397 (also, elevation is 526 m)

def time_params():

    """ Gathers the date and time values required for position.
    
    Returns:
    string: today's date
    Current time

    """
    cal_day = datetime.date.today().strftime("%Y-%m-%d")

    ##############################################
    ### PICK IT UP HERE - NEED THE TIME VALUES ###
    ##############################################
    
    print(cal_day)
    print(type(cal_day))

time_params()

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

    loc_lat, loc_lon = get_location()
    astronomy_api = ("https://api.astronomyapi.com/api/v2/bodies/positions/sun")
    let_me_in = (constant1, constant2)
    values = {  "latitude": loc_lat,
                "longitude": loc_lon,
                "elevation": str(526), # in meters
                "from_date": str('2017-12-20'),
                "to_date": str('2017-12-20'),
                "time": "08:00:00" }
    response = requests.get(astronomy_api, auth=let_me_in, params=values)
    response_data = json.loads(response.content)
    position = response_data["data"]["table"]["rows"][0]["cells"][0]["position"]["horizontal"]
    altitude = position["altitude"]["degrees"]
    azimuth = position["azimuth"]["degrees"]
    return azimuth, altitude

get_sun_position()

def print_position():

    """ Prints the position of the sun in the sky using the supplied coordinates
        Parameters:
        azimuth (float)
        altitude (float)
        Returns:
        print statement
    """
    azimuth, altitude = get_sun_position()
    return f'The Sun is currently at {azimuth} degrees azimuth and {altitude} degrees altitude.'

print_position()

if __name__ == "__main__":
    ip_location = get_location()
    body_position = get_sun_position()
    output = print(print_position())



# get_sun_position is working with test values.  Need to refine.

# get_location is now working and returns the desired values.  Copied into solar.py
