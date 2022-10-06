#!/bin/env python3

####################################################################
### THIS PRODUCES OUTPUT THAT DOES NOT MATCH OTHER DATA SOURCES. ###
### FURTHER RESEARCH IS NEEDED TO VALIDATE DATA BEING CAPTURED   ###
### FROM THE API USED IN FUNCTION 'get_sun_position'.            ###
####################################################################

####################################################################
### I HAD get_location WORKING TOO, BUT SOMEHOW BLEW IT UP.      ###
# #################################################################### 

import datetime
from datetime import date
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
    return latitude, longitude

get_location()


# test lat/lon values:  47.6987, -117.4397 (also, elevation is 526 m)
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

    today = date.today()
    #current_time = datetime.now().strftime("%H:%M:%S")
    astronomy_api = ("https://api.astronomyapi.com/api/v2/bodies/positions/sun")
    let_me_in = (constant1, constant2)
    values = {  "latitude": str(latitude),
                "longitude": str(longitude),
                "elevation": str(526), # in meters
                "from_date": str(today),
                "time": ('15:00:00')
                }
                #"to_date": str('2022-10-06')}
    response = requests.get(astronomy_api, auth=let_me_in, params=values)
    response_data = json.loads(response.content)
    position = response_data["data"]["table"]["rows"][0]["cells"][0]["position"]["horizontal"]
    altitude = position["altitude"]["degrees"]
    azimuth = position["azimuth"]["degrees"]
    #print(f'The Sun is currently at altitude {altitude} and azimuth {azimuth}.')
    return azimuth, altitude

get_sun_position()

def print_position(azimuth, altitude):

    """ Prints the position of the Sun at the specified coordinates.
    
        Params:  data from functions 'get_location' and 'get_sun_position'.
        Returns:  print to stdout.
    """

    print(f'The location from which the sun is being observed is {latitude} degrees North, and {longitude} degrees West.')
    print(f'From that location, the Sun is visible at azimuth {azimuth} and altitude {altitude}.')

if __name__ == "__main__":
    
    latitude, longitude = get_location()
    azimuth, altitude =  get_sun_position()
    print_position(azimuth, altitude)