import csv

with open('data/Carto_MacysPolygonsFinal.csv') as f:
    reader = csv.reader(f)
    #headers = next(readCSV)[1:]
    #print headers
    for row in reader:
        print(" ".join(row))
    print reader[0]

    while row in reader ==
