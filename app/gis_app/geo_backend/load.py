import os

from django.contrib.gis.utils import LayerMapping
from .models import PowerPlant, WorldStates


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


def run_plants(verbose=True):
    lm = LayerMapping(PowerPlant, plant_file, power_plant_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)



# Auto-generated `LayerMapping` dictionary for WorldStates model
worldstates_mapping = {
    'featurecla': 'featurecla',
    'scalerank': 'scalerank',
    'labelrank': 'LABELRANK',
    'sovereignt': 'SOVEREIGNT',
    'sov_a3': 'SOV_A3',
    'adm0_dif': 'ADM0_DIF',
    'level': 'LEVEL',
    'type': 'TYPE',
    'admin': 'ADMIN',
    'adm0_a3': 'ADM0_A3',
    'geou_dif': 'GEOU_DIF',
    'geounit': 'GEOUNIT',
    'gu_a3': 'GU_A3',
    'su_dif': 'SU_DIF',
    'subunit': 'SUBUNIT',
    'su_a3': 'SU_A3',
    'brk_diff': 'BRK_DIFF',
    'name': 'NAME',
    'name_long': 'NAME_LONG',
    'brk_a3': 'BRK_A3',
    'brk_name': 'BRK_NAME',
    'brk_group': 'BRK_GROUP',
    'abbrev': 'ABBREV',
    'postal': 'POSTAL',
    'formal_en': 'FORMAL_EN',
    'formal_fr': 'FORMAL_FR',
    'name_ciawf': 'NAME_CIAWF',
    'note_adm0': 'NOTE_ADM0',
    'note_brk': 'NOTE_BRK',
    'name_sort': 'NAME_SORT',
    'name_alt': 'NAME_ALT',
    'mapcolor7': 'MAPCOLOR7',
    'mapcolor8': 'MAPCOLOR8',
    'mapcolor9': 'MAPCOLOR9',
    'mapcolor13': 'MAPCOLOR13',
    'pop_est': 'POP_EST',
    'pop_rank': 'POP_RANK',
    'gdp_md_est': 'GDP_MD_EST',
    'pop_year': 'POP_YEAR',
    'lastcensus': 'LASTCENSUS',
    'gdp_year': 'GDP_YEAR',
    'economy': 'ECONOMY',
    'income_grp': 'INCOME_GRP',
    'wikipedia': 'WIKIPEDIA',
    'fips_10_field': 'FIPS_10_',
    'iso_a2': 'ISO_A2',
    'iso_a3': 'ISO_A3',
    'iso_a3_eh': 'ISO_A3_EH',
    'iso_n3': 'ISO_N3',
    'un_a3': 'UN_A3',
    'wb_a2': 'WB_A2',
    'wb_a3': 'WB_A3',
    'woe_id': 'WOE_ID',
    'woe_id_eh': 'WOE_ID_EH',
    'woe_note': 'WOE_NOTE',
    'adm0_a3_is': 'ADM0_A3_IS',
    'adm0_a3_us': 'ADM0_A3_US',
    'adm0_a3_un': 'ADM0_A3_UN',
    'adm0_a3_wb': 'ADM0_A3_WB',
    'continent': 'CONTINENT',
    'region_un': 'REGION_UN',
    'subregion': 'SUBREGION',
    'region_wb': 'REGION_WB',
    'name_len': 'NAME_LEN',
    'long_len': 'LONG_LEN',
    'abbrev_len': 'ABBREV_LEN',
    'tiny': 'TINY',
    'homepart': 'HOMEPART',
    'min_zoom': 'MIN_ZOOM',
    'min_label': 'MIN_LABEL',
    'max_label': 'MAX_LABEL',
    'ne_id': 'NE_ID',
    'wikidataid': 'WIKIDATAID',
    'name_ar': 'NAME_AR',
    'name_bn': 'NAME_BN',
    'name_de': 'NAME_DE',
    'name_en': 'NAME_EN',
    'name_es': 'NAME_ES',
    'name_fr': 'NAME_FR',
    'name_el': 'NAME_EL',
    'name_hi': 'NAME_HI',
    'name_hu': 'NAME_HU',
    'name_id': 'NAME_ID',
    'name_it': 'NAME_IT',
    'name_ja': 'NAME_JA',
    'name_ko': 'NAME_KO',
    'name_nl': 'NAME_NL',
    'name_pl': 'NAME_PL',
    'name_pt': 'NAME_PT',
    'name_ru': 'NAME_RU',
    'name_sv': 'NAME_SV',
    'name_tr': 'NAME_TR',
    'name_vi': 'NAME_VI',
    'name_zh': 'NAME_ZH',
    'geom': 'MULTIPOLYGON',
}

states_file = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'ne_50m_admin_0_countries.shp'),
)


def run_states(verbose=True):
    lm = LayerMapping(WorldStates, states_file, worldstates_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
