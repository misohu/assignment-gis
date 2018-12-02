import json

from django.shortcuts import render
from django.db import connections
from django.db import connection
from django.core.serializers import serialize

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import PowerPlant

def default_map(request):
    res_dict = json.loads(serialize('geojson', PowerPlant.objects.all(),
    geometry_field='mpoly', fields=('shp_id', 'name', 'link', 'built', 'image')))
    for index, i in enumerate(res_dict['features']):
        i['id'] = index
        i['properties']['description'] = "<div><strong>Link:</strong> <a href ="+ i['properties']['link']+">"+i['properties']['link']+"</a></div><div><strong>Built in:</strong> " + str(int(i['properties']['built'])) + "</div><img src=" + i['properties']['image']+ " width=200 height=200>"
        i['properties']['icon'] = 'marker'
    # print(json.dumps(res_dict))
    return render(request, 'default.html', 
      {
        'mapbox_access_token':"pk.eyJ1IjoicG9jaWsiLCJhIjoiY2pta2p6ejg3MGp6ejNrcXN2Z29zOGZwNCJ9.jDCPW258dliRWnmoe9t8PQ",
        "plants": json.dumps(res_dict),
        "reactor_list": PowerPlant.objects.all()
      })

@api_view(['GET'])
def get_polygon(request):
   lon = request.GET.get('lon', 0)
   lat = request.GET.get('lat', 0)
   connection = connections['default']
   cursor = connection.cursor()
   cursor.execute('''
        SELECT ST_AsGeoJSON(st_buffer( ST_GeomFromText('POINT({} {})')::geography, 500000, 'quad_segs=8'));
        '''.format(lon, lat))
   area_air = json.loads(cursor.fetchall()[0][0])
   cursor.execute('''
        SELECT ST_AsGeoJSON(st_buffer( ST_GeomFromText('POINT({} {})')::geography, 30000, 'quad_segs=8'));
        '''.format(lon, lat))
   area_explosion = json.loads(cursor.fetchall()[0][0])

   print(lon, lat)
   print(area_air)
   return Response({
       'polygon_air': area_air,
       'polygon_explosion': area_explosion,
       })


@api_view(['GET'])
def get_surroundings(request):
   lon = request.GET.get('lon', 0)
   lat = request.GET.get('lat', 0)
   connection = connections['default']
   cursor = connection.cursor()
   cursor.execute('''
        SELECT name, lat, lon, shp_id, st_distance(point::geography, g.mpoly::geography) as dist
        FROM geo_backend_powerplant as g,  ST_GeomFromText('POINT({} {})') as point
        WHERE st_intersects(
            st_buffer(point::geography, 500000, 'quad_segs=8'),
            g.mpoly::geography)
        ORDER BY dist;
        '''.format(lon, lat))
   x = cursor.fetchall()
   print(x)
   return Response({
        "plants": list(map(lambda f: {
            "name": f[0],
            "lat": f[1],
            "lon": f[2],
            "shp_id": f[3],
            "dist": f[4]}, x))
    })

@api_view(['GET'])
def get_all_buffers(request): 
    connection = connections['default']
    cursor = connection.cursor()
    cursor.execute('''
        SELECT DISTINCT ST_AsGeoJSON(st_buffer(mpoly::geography, 500000, 'quad_segs=8')) 
        FROM geo_backend_powerplant;
        ''')
    x = cursor.fetchall()
    return Response(
      {'all_plants': list(map(lambda x: {"type": "Feature", "geometry": json.loads(x[0])}, x))})

@api_view(['GET'])
def get_states(request): 
    '''
    Tabel state_reactors was created with
      CREATE TABLE state_reactors AS
      SELECT states.sovereignt, count(*) as count
      FROM geo_backend_worldstates as states
      JOIN geo_backend_powerplant as plants
      ON st_intersects(
        states.geom, st_buffer(
          plants.mpoly::geography, 500000, 'quad_segs=8'))
      GROUP BY states.sovereignt
    '''
    connection = connections['default']
    cursor = connection.cursor()
    cursor.execute('''
        SELECT *
        FROM state_reactors
        ORDER BY count desc
        ''')
    x = cursor.fetchall()
    return Response(
      {'all_states': list(map(lambda x: {"state": x[0], "count": x[1]}, x))})

@api_view(['GET'])
def get_state(request):
    name = request.GET.get('state', 0)
    connection = connections['default']
    cursor = connection.cursor()
    cursor.execute('''
        SELECT ST_AsGeoJSON(geom), ST_AsGeoJSON(ST_Centroid(geom))
        FROM geo_backend_worldstates
        WHERE sovereignt like '{}'
        ORDER BY st_area(geom) desc
        LIMIT 1
        '''.format(name))
    x = cursor.fetchall()
    return Response(
      {'state': {"type": "Feature", "geometry": json.loads(x[0][0])},
       'centroid': json.loads(x[0][1])})