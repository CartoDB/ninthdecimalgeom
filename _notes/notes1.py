import csv

with open('data/Carto_MacysPolygonsFinal.csv', 'r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    print readCSV
    headers = next(readCSV)[1:]
    print headers
    for line in readCSV:
        print line


        
