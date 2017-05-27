from cartodb import CartoDBAPIKey, CartoDBException, FileImport
import pandas as pd
from datetime import datetime

def add(cartojson='',first='',second=''):
  print(' input file from form ',  request.form.get("cartojson"))
  print(' input file from userame  ',  request.form.get("userName"))
  if cartojson == '':
      cartojson = request.form.get("cartojson")
  if first == '':
      first = request.form.get("userName")
  if second == '':
      second = request.form.get("apiKey")
  # result = first + second
  #df = pd.read_csv(cartojson)
  #print df.head()
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

  df = pd.read_csv(inFile)
  print('THIS IS THE FILE', inFile)
  #df = pd.read_excel(inFile, sheetname=0)

  df = df[df.geofence.notnull()]
  #df = df.drop('the_geom',axis=1)

  df['the_geom'] = df['geofence'].map(reorderLatLng)
  df = df.rename(columns=lambda x: x.replace('latitude', 'centroid_latitude').replace('longitude', 'centroid_longitude'))
  curTime = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
  ouFile = 'data/ninth_decimal_'+'_'+curTime+'.csv'

  df.to_csv(ouFile,index=False)
  cl = CartoDBAPIKey(apikey, username)
  
  # Import csv file, set privacy as 'link' and create a default viz
  fi = FileImport(ouFile, cl, create_vis='false', privacy='link')
  fi.run()
  return fi