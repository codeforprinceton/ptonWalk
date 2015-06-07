import osmapi
from shapely.geometry import LineString, Point, Polygon
from descartes.patch import PolygonPatch
import numpy as np
import pandas

## USER INPUT

effic = 0.9
time= 10 # minutes

# Bounding Box For Princeton, NJ
mnlon=-74.723 # minimum longitude in degE
mnlat=40.316 # minimum latitude in degN
mxlon=-74.626 # maximum longitude in degE
mxlat=40.382 # maximum latitude in degN

## END USER INPUT

pi_180=np.pi/180.
re=6371.e3
degtom=re*np.cos(pi_180*40.35)*pi_180
metersToDeg=1.0/degtom
speed_km = 5.e3 # From Wikipedia (m/hr)
speed=speed_km*effic/60. # units are meters / minute
dist=speed*time

api=osmapi.OsmApi()
mp=api.Map(min_lon=mnlon,min_lat=mnlat,max_lon=mxlon,max_lat=mxlat)

PARKS=[]
for rec in mp:
    if rec['type'] == 'way':
        tags=rec['data']['tag']
        if tags.has_key('leisure'):
            if tags['leisure'] == 'park':
                if tags.has_key('name'):
                    PARKS.append((rec['data']['id'],tags['name']))
                else:
                    PARKS.append((rec['data']['id'],'noname'))

df=pandas.read_csv('PrincetonBlockLot-geocoded.csv')
house_lons=df.longitude
house_lats=df.latitude

print 'Walking efficiency = ',effic
print 'Time(minutes) = ',time

for node,name in PARKS:
    way=api.WayGet(node)
    coords=[]
    for nd in way['nd']:
        n=api.NodeGet(nd)
        coords.append((n['lon'],n['lat']))

    x,y= zip(*coords)
    poly=Polygon(zip(x,y))
    path=LineString(zip(x,y))
    dilated=path.buffer(dist*metersToDeg)
    try:
        patch=PolygonPatch(dilated)
    except AssertionError:
        pass
        continue

    tot=0
    for c in zip(house_lons,house_lats):
        if c[0]=='range':
            continue
        try:
            lon=np.float(c[0])
        except ValueError:
            continue
        try:
            lat=np.float(c[1])
        except ValueError:
            continue
        if np.isfinite(lon) and np.isfinite(lat):
            pt=Point(lon,lat)
            if pt.intersects(dilated):
                 tot=tot+1

    print 'Total of :',tot,' homes in walking distance to ',name

    
