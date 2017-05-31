from cartodb import CartoDBAPIKey, CartoDBException, FileImport
#import pandas as pd #remove pandas b/c dokku doesn't seem to support numpy's C dependencies
import csv
from datetime import datetime
from io import TextIOWrapper
import StringIO

def add(cartojson='',first='',second=''):
    print(' input file from form ',  request.form.get("cartojson"))
    print(' input file from userame  ',  request.form.get("userName"))
    if cartojson == '':
        cartojson = request.form.get("cartojson")
    if first == '':
        first = request.form.get("userName")
    if second == '':
        second = request.form.get("apiKey")

    print cartojson
    filepath = os.path.join(os.path.dirname(__file__)+'/data/input',cartojson)
    print filepath
    open_read = open(filepath,'r')

    result = cleanNinthDecimal(open_read,first,second)
    return render_template("index.html",result=result)

def reorderLatLng(inValue): 
    listCoords = []
    for i in inValue.split(','):
        i = i.replace('((','').replace('))','').replace('POLYGON','')
        i = i.split(' ')
        inPair = i[1].replace("'",'')+' '+i[0].replace("'",'')
        listCoords.append(inPair)
    print 'listCoords:',listCoords
    return "POLYGON(("+','.join(listCoords)+"))"

def cleanNinthDecimal(inFile,username,apikey):
    curTime = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    ouFile = 'data/ninth_decimal_'+curTime+'.csv'
    
    #with open(inFile) as csvinput:
    # x = []
    # for i in csvinput:
    #     x.append(i)
    #import pdb
    #pdb.set_trace()
    with open(ouFile, 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')

        # This code opens our bytestream with \r as the newline
        newline_wrapper = TextIOWrapper(inFile, newline='\r')

        reader = csv.reader(newline_wrapper) #, delimiter = ',')#, lineterminator='\r')

        all = []
        row = next(reader)
        row[7] = 'centroid_latitude'
        row[8] = 'centroid_longitude'
        row.append('the_geom')
        all.append(row)

        for row in reader:
            row.append(reorderLatLng(row[11]))
            all.append(row)

        writer.writerows(all)

    
    cl = CartoDBAPIKey(apikey, username)
  
    #Import csv file, set privacy as 'link' and create a default viz
    fi = FileImport(ouFile, cl, create_vis='false', privacy='link')
    fi.run()
    return fi