#!/bin/env python3

""" Scratchpad - WIP.  Functions in main script, breaking out for unit testing
    Need to verify as standalone function. """

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
        float:  latitude
        float:  longitude

        Note:  The IP below in "target" is a local entry for accuracy.
        The URL format is based on the value required by the API.
        If this is run from a VM, it will return the location of the data center.
    """
    target = requests.get('http://ip-api.com/json/174.31.14.127?fields=lat,lon')
    target_data = json.loads(target.text)
    latitude = (target_data['lat'])
    longitude = (target_data['lon'])
    return latitude,longitude

get_location()