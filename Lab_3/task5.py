# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:45:26 2015

@author: daraperl
"""

import json
import sys
import csv

if __name__=='__main__':
    jsonFile = open(sys.argv[1], 'r')
    data = json.load(jsonFile)
    stations = data['stationBeanList']
    
    with open(sys.argv[2], 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Station Name', 'Latitude', 'Longitude'])
    
        for s in stations:
            if s['statusKey'] != '1' and s['stationName'].startswith('Coming soon'):
                stationName = s['stationName'][13:]
                stationLat = s['latitude']
                stationLong = s['longitude']
                row = [stationName, stationLat, stationLong]
                writer.writerow(row)
                