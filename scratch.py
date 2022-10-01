#!/bin/env python3

# """Scratchpad"""

from pprint import pprint
import requests
import json


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



    # add return values here when available
    # return None, None

# def get_sun_position(latitude, longitude):
#     # future enhancement - add options for other "local" bodies in our solar system. input? menu option?
#     #  
#     now = datetime.now().strftime("%H:%M:%S")
#     today = date.today()
#     auth = ASTRONOMYAPI_ID,ASTRONOMYAPI_SECRET
#     # requirements for the API
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