#!/bin/env python3

""" Scratchpad - WIP.  Functions in main script, breaking out for unit testing
    Need to verify as standalone function."""

### 10-22-2022:  functionality confirmed.  ###

# import datetime
# import time
# import json
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
        accuracy.  The URL format is based on the value required by the
        API.  If this is run from a VM without that manual entry, it
        will return the location of the data center.
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """
    target = requests.get('http://ip-api.com/json/174.31.14.127?fields=lat,lon')
    target_data = target.json()
    latitude = str(target_data['lat'])
    longitude = str(target_data['lon'])
    print(latitude, longitude)
    return (latitude,longitude)

get_location()
