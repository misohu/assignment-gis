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
    geometry_field='mpoly', fields=('shp_id', 'name', 'link',)))
    for index, i in enumerate(res_dict['features']):
        i['id'] = index
        i['properties']['description'] = i['properties']['link']
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
        SELECT ST_AsGeoJSON(st_buffer( ST_GeomFromText('POINT({} {})')::geography, 1100000, 'quad_segs=8'));
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
        SELECT name
        FROM geo_backend_powerplant 
        WHERE st_intersects(
                st_buffer(ST_GeomFromText('POINT({} {})')::geography, 1100000, 'quad_segs=8'),
                mpoly::geography);
        '''.format(lon, lat))
   x = cursor.fetchall()
   print(x)
   return Response({
        "plants": list(map(lambda f: f[0], x))
    })