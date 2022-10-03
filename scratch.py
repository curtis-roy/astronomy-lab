#!/bin/env python3

"""Scratchpad"""

import datetime
import json
from pprint import pprint
import requests
from constants import constant1, constant2

# test lat/lon values:  47.6987, -117.4397 (also, elevation is 526 m)
#def get_sun_position(latitude, longitude):
def get_sun_position():
    """ """

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
    #response_data = json.loads()
    pprint(response_data)


# now I need to use csvkit to put the JSON output into a spreadsheet, then filter out the extra stuff.  see line 24 and 25

get_sun_position()
    #now = datetime.now().strftime("%H:%M:%S")
    # today = date.today()
    
    # # requirements for the API
#     payload = { "latitude" : float(latitude),
#                 "longitude" : float(longitude),
#                 "elevation" : "50", # might or might not be required
#                 "from_date" : today,
#                 "to_date" : today,
#                 "time" : now,
#                 }
#     url = 'https://api.astronomyapi.com/api/v2/bodies/positions/sun'
#     response = requests.get(url,auth=auth,params=payload)
#     data = response.json()
#     position = data["data"]["table"]["rows"][0]["cells"][0]["position"]["horizontal"]
#     altitude = position["altitude"]["degrees"]
#     azimuth = position["azimuth"]["degrees"]
#     return azimuth,altitude

#     # second one is the non broken apart its for the altitude, you'd just change altitude to azimuth
#     # response.json()["data"]["table"]["rows"][0]["cells"][0]["position"]["horizontal"]["altitude"]["degrees"]



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
