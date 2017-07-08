#! python3
# -*- coding:utf-8 -*-
from pygal.maps.world import World

wm = World()
wm.title = 'Populations of Countres in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.render_to_file('na_populations.svg')