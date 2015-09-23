# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:30:01 2015

@author: daraperl
"""

import datetime
import json
import sys

if __name__=='__main__':
    jsonFile = open(sys.argv[1], 'r')
    metadata = json.load(jsonFile)
    print datetime.datetime.fromtimestamp(metadata['createdAt'])