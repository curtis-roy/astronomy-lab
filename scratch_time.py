#!/bin/env python3

""" Scratchpad - functions in main script, breaking out for
    unit testing as a standalone function.  Needs to be verified"""

import datetime
import time
# import json
# import requests
# from constants import constant1, constant2

def time_params():

    """ Gathers the date and time values required for position.

    Returns:
    str: today's date
    str: current time

    """

    cal_day = datetime.date.today().strftime("%Y-%m-%d")
    time_now = time.strftime("%H:%M:%S")

    return cal_day, time_now

time_params()