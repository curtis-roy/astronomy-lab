#!/bin/env python3

"""Get the sun's position in the sky"""

import datetime
import requests


#### Move these to external location ASAP ####
ASTRONOMYAPI_ID = "<yourapiid>"
ASTRONOMYAPI_SECRET = "<yourapisecretkey>"

###############################
####  PICK IT BACK UP HERE ####
###############################

def get_location():
    """ Returns the longitude and latitude for the location of this IP.
        
        Returns:
        str:  latitude
        str:  longitude
        """
    response = requests.get(f'http://ip-api.com/json/174.31.14.127?fields=status,message,regionName,city,lat,lon,timezone,offset,query')
    response_dict = response.json()


    # add return values here when available
    return None, None

def get_sun_position(latitude, longitude):
    """Returns the current position of the sun in the sky at the specified location.

    Parameters:
    latitude (str)
    longitude (str)

    Returns:
    float: azimuth
    float: altitude
    """

    # add return values here when available
    return 0, 0

def print_position(azimuth, altitude):
    """Prints the position of the sun in the sky using the supplied coordinates
    
    Parameters:
    azimuth (float)
    altitude (float)
    """

    print('The Sun is currently at: ')

if __name__ == "__main__":
    latitude, longitude = get_location()
    azimuth, altitude = get_sun_position()
    print_position(azimuth, altitude)

""" 'Always know where your towel is.'  --Ford Prefect """

