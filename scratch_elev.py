#!/bin/env python3

""" Scratchpad - not yet functional. Something wrong with
    the JSON data being received """

# import datetime
# import time
import json
import requests
# from constants import constant1, constant2

def get_location():
    """ Gathers the longitude and latitude for the location of an IP.
        Parameter:
        IP address

        Returns:
        float:  latitude (converted to str for actual use)
        float:  longitude (converted to str for actual use)
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Note:  The IP below in "target" is a local entry to confirm
        accuracy with external sources.  The URL format is based on the
        value required by the API.  If this is run from a VM without
        that manual entry, it may return the location of the data center.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    target = requests.get('http://ip-api.com/json/174.31.14.127?fields=lat,lon')
    target_data = target.json()
    latitude = str(target_data['lat'])
    longitude = str(target_data['lon'])
    return (latitude,longitude)

get_location()

##########################################################
### get_location IS WORKING, BUT get_elevation IS NOT. ###
### HAVING TROUBLE PARSING THE RETURN FROM THE API.    ###
##########################################################

def get_elevation():
    """ Gathers the elevation at a specified latitude / longitude.

        Returns:
        <type?>:  elevation
    """
    # loc_lat, loc_lon = get_location()
    # values = loc_lat, loc_lon
    # elevation_api = ('https://api.open-elevation.com/api/v1/lookup?locations=')
    target = requests.get('https://api.open-elevation.com/api/v1/lookup?locations=47.65,117.42')
    # target = requests.get(elevation_api, params=values)
    target_data = target.json()
    raw_target_data = target_data["results"]
    print(raw_target_data)
    print(type(raw_target_data))
    #print(target_data)
    # return raw_target_data

get_elevation()
