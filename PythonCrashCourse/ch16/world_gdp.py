#! python3
# -*- coding:utf-8 -*-
import json
from country_codes import get_country_code
from pygal.maps.world import World
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

# open the gdp file
with open('gdp.json') as f:
    gdps = json.load(f)

cc_gdp = {}
for gdp in gdps:
    if gdp['Year'] == '2014':
        country_name = gdp['Country Name']
        gdp = int(float(gdp['Value']))
        code = get_country_code(country_name)
        if code:
            cc_gdp[code] = gdp

wm_style = RS('#446633', base_style=LCS)
wm = World(style=wm_style)
wm.title = 'World GDP Of 2014'

wm.add('world gdp', cc_gdp)
wm.render_to_file('world_gdp.svg')