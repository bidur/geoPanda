# Read Polygons from geojson file (OSM data)

import json
from shapely.geometry import Polygon

def osmFeature2Polygon(ringList): # only handles the first polygon ( ignores hole polygons for now)
	polyCoord = []
	for ring1 in ringList[0][0]:
		
		#print ring1 
		
		polyCoord.append((ring1[0],ring1[1]))
	poly1 = Polygon(polyCoord)
	return  poly1

############################################	
def getOSMPolygons( INPUTFILE ):

	clustFile = open(INPUTFILE,'r')
	data = json.load(clustFile)

	polygonDict = {} # dict of cluster data ( each cluster is a list of pointCount, pointPercent, Polygon)

	for feature in data['features']:
		
		#print feature['properties']['name']
		#print feature['properties']['osm_id']
		polygonAOI = osmFeature2Polygon (feature['geometry']['coordinates'])
		
		# e.g. polygonDict[osm_id] = list of building name and polygonObject
		polygonDict[ feature['properties']['osm_id'] ] =  [ feature['properties']['name'],  polygonAOI ]
	
	return polygonDict

############################################	


INPUTFILE = 'osm_tourism/tourism_nepal_Poly.geojson'


osmPolygonDict = getOSMPolygons( INPUTFILE ) #key= osm_id, value = [name, polygon object]

for pid in osmPolygonDict.keys():
	print osmPolygonDict[pid][0]
