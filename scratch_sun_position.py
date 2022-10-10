#!/bin/env python3

""" Scratchpad - tested functional as of 10/10/2022 3:00 PM.
    Accuracy of altitude / azimuth returns not verified """

# import datetime
# import time
import json
import requests
from constants import constant1, constant2

def get_sun_position():

    """ Returns the current position of the Sun in the sky at
        the specified location.

        Parameters:
        latitude (str)
        longitude (str)
        elevation (str)
        Returns:
        float:  altitude
        float:  azimuth
    """

    # loc_lat, loc_lon = get_location() # function 'get_location' in main script
    loc_lat = 47.65 # test values
    loc_lon = 117.42 # test values
    # cal_day, time_now = time_params() # function 'get_time' in main script
    cal_day = "2022-10-10" # test values
    time_now = "08:00:00" # test values
    loc_elev = 526 # elevation in meters, work on elevation API in progress
    astronomy_api = ("https://api.astronomyapi.com/api/v2/bodies/positions/sun")
    let_me_in = (constant1, constant2)
    values = {  "latitude": loc_lat,
                "longitude": loc_lon,
                "elevation": loc_elev,
                "from_date": cal_day,
                "to_date": cal_day,
                "time": time_now }
    response = requests.get(astronomy_api, auth=let_me_in, params=values)
    response_data = json.loads(response.content)
    position = response_data["data"]["table"]["rows"][0]["cells"][0]["position"]["horizontal"]
    altitude = position["altitude"]["degrees"]
    azimuth = position["azimuth"]["degrees"]
    print(azimuth, altitude)
    return azimuth, altitude

get_sun_position()
