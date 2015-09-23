# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 14:52:08 2015
PUI2015 - dp1618 - hw 2 due 9/23/15
@author: daraperl
"""

import json
import sys
import urllib2

if __name__=='__main__':
    # access the MTA Bus times website and store the information in a file
    url = ('http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s'
        % (sys.argv[1], sys.argv[2]))
    request = urllib2.urlopen(url)
    metadata = json.load(request)
    busses = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    #initialize the number of busses and an array to store the busses in    
    NumberBusses = 0
    Stored = []
   
    #find the station latitude and longitude and store in Stored
    for s in busses:
        stationLat = s['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        stationLong = s['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        row = [NumberBusses, stationLat, stationLong]
        Stored.append(row)
        NumberBusses += 1
    
    #Print the busline being accessed
    print 'Bus Line %s' % sys.argv[2]
    #print the number of active busses
    print 'The number of active busses on this bus line is %s' % NumberBusses
    row = 0
    #print the latitude and longitude of each bus saved in stored
    for r in Stored:
        print 'Bus %s is at Latitude %s and Longitude %s' % (Stored[row][0], Stored[row][1], Stored[row][2])
        row += 1