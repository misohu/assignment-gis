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
    geometry_field='mpoly', fields=('name', 'link',)))
    for i in res_dict['features']:
        i['properties']['description'] = i['properties']['link']
        i['properties']['icon'] = 'theatre'
    return render(request, 'default.html', 
            {'mapbox_access_token':"pk.eyJ1IjoicG9jaWsiLCJhIjoiY2pta2p6ejg3MGp6ejNrcXN2Z29zOGZwNCJ9.jDCPW258dliRWnmoe9t8PQ",
                "plants": json.dumps(res_dict)})

@api_view(['GET'])
def get_polygon(request):
   lon = request.GET.get('lon', 0)
   lat = request.GET.get('lat', 0)
   connection = connections['default']
   cursor = connection.cursor()
   cursor.execute('''
        SELECT ST_AsGeoJSON(
            ST_AsText(
                st_buffer(
                    ST_MakePoint(%s, %s), 50, 'quad_segs=8')
                )
            );
        ''', [lon, lat])
   return Response({'polygon': json.loads(cursor.fetchall()[0][0])})
