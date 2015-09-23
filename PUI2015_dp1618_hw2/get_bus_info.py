# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 12:03:03 2015

@author: daraperl
"""
#import libraries to be used
import json
import sys
import urllib2
import csv

if __name__=='__main__':
    # access the MTA Bus times website and store the information in a file
    url = ('http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s'
        % (sys.argv[1], sys.argv[2]))
    request = urllib2.urlopen(url)
    metadata = json.load(request)
    busses = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    #open a CSV file and add the column headings 
    with open(sys.argv[3], 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Latitude', 'Longitude', 'Station Name','Station Status'])
        #for each bus of the bus line specified above, find the station latitude, 
        #longitude, name and status. 
        for s in busses:
            stationLat = s['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            stationLong = s['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
            if s['MonitoredVehicleJourney']['OnwardCalls'] == {}:
                StationName = 'NA'
                StationStatus = 'NA'
            else:
                StationName = s['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
                StationStatus = s['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
            #store the latitude, longitude, station name and status in an array
            row = [stationLat, stationLong, StationName, StationStatus]
            #add row to the csv file.             
            writer.writerow(row)
#                