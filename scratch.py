#!/bin/env python3

"""Scratchpad"""

import datetime
import requests
from requests.auth import HTTPBasicAuth
from constants import constant1, constant2
import json

#eochair = constant1
#runda = constant2

def get_sun_position(latitude, longitude):

    astronomy_api = ("https://api.astronomyapi.com/api/v2/bodies/positions/sun")
    response = requests.get(astronomy_api, auth=HTTPBasicAuth(constant1, constant2))
    response_data = json.loads(response.text)
    print(response_data)


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