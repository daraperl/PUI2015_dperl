# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:44:27 2015

@author: daraperl
"""

import json
import sys

if __name__=='__main__':
    jsonFile = open(sys.argv[1], 'r')
    data = json.load(jsonFile)
    stations = data['stationBeanList']
    
    for s in stations:
        if s['statusKey'] != '1' and s['stationName'].startswith('Coming soon'):
            stationName = s['stationName'][13:]
            stationLat = s['latitude']
            stationLong = s['longitude']
            print '%s: %s, %s' % (stationName, stationLat, stationLong)