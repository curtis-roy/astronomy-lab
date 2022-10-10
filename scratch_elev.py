#!/bin/env python3

""" Scratchpad - not yet functional. Something wrong with either
    the JSON data being received or something with the requests.get
    being sent to the API. JSONDecodeError("Expecting value", s, err.value) from None
     json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0) """

# import datetime
# import time
import json
import requests
# from constants import constant1, constant2

def get_elevation():
    """ Gathers the elevation at a specified latitude / longitude.

        Returns:
        <type?>:  elevation
    """
    #loc_lat, loc_lon = get_location()
    #values = (str(loc_lat)), (str(loc_lon))
    #elevation_api = ('https://api.open-elevation.com/api/v1/lookup?locations=47.65,117.42)
    target = requests.get('https://api.open-elevation.com/api/v1/lookup?locations=47.65,117.42')
    #target = requests.get(elevation_api, params=values)
    target_data = json.loads(target.content)
    elevation = (target_data["elevation"])
    print(elevation)
    return elevation

get_elevation()
