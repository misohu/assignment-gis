import os

from django.contrib.gis.utils import LayerMapping
from .models import PowerPlant


power_plant_mapping = {
    "shp_id" : "ID",
    "name" : "Name",
    "plant" : "Plant",
    "country" : "Country",
    "total_power" : "TotalPower",
    "type_of" : "Type",
    "status" : "Status",
    "power_mw" :"PowerMW",
    "power_cat" : "PowerCat",
    "built" : "Built",
    "connected" : "Connected",
    "link" : "Link",
    "lon" : "Lon",
    "lat" : "Lat",
    "elev" : "Elev",
    "image" : "Image",
    'mpoly' : "POINT"
}


plant_file = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'NuclearReactors2011.shp'),
)


def run(verbose=True):
    lm = LayerMapping(PowerPlant, plant_file, power_plant_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
