import csv
with open('data/Carto_MacysPolygonsFinal.csv', "rb") as f:
    reader = csv.reader(f)
    i = reader.next()
    #rest = [row for row in reader]
    geoFenceColLoc = i.index('geofence')

import csv
with open('data/example.csv', "rb", ) as f:
    reader = csv.reader(f)
    i = reader.next()
    #rest = [row for row in reader]
    geoFenceColLoc = i.index('geofence')
