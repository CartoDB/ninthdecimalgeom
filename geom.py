from cartodb import CartoDBAPIKey, FileImport  # CartoDBException, FileImport
# import pandas as pd #remove pandas b/c dokku doesn't seem to support numpy's C dependencies
import csv
from datetime import datetime
from io import TextIOWrapper
# import StringIO
# import os
# from requests import request
# from flask import render_template   # Flask, send_file, render_template


def reorderLatLng(inValue):
    listCoords = []
    for i in inValue.split(','):
        i = i.replace('((', '').replace('))', '').replace('POLYGON', '')
        i = i.split(' ')
        inPair = i[1].replace("'", '')+' '+i[0].replace("'", '')
        listCoords.append(inPair)
    print 'listCoords:', listCoords
    return "POLYGON(("+','.join(listCoords)+"))"


def cleanNinthDecimal(inFile, inFileName, username, apikey):
    curTime = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    ouFileName = inFileName.replace('.csv', '')
    ouFile = 'data/ninth_decimal_'+curTime+'.csv'
    ouFile = 'data/_send/'+ouFileName+'.csv'

    with open(ouFile, 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')

        # This code opens our bytestream with \r as the newline
        newline_wrapper = TextIOWrapper(inFile, newline=None)  # newline='\r')

        reader = csv.reader(newline_wrapper)  # , delimiter = ',')#, lineterminator='\r')

        all = []
        row = next(reader)

        row.append('the_geom')
        all.append(row)

        geoFenceColLoc = row.index('geofence')

        for row in reader:
            row.append(reorderLatLng(row[geoFenceColLoc]))
            all.append(row)

        writer.writerows(all)

    cl = CartoDBAPIKey(apikey, username)

    # Import csv file, set privacy as 'link' and create a default viz
    fi = FileImport(ouFile, cl, create_vis='false', privacy='link', content_guessing='false', type_guessing='false')
    fi.run()
    return fi
