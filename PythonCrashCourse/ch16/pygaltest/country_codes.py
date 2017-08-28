#! python3
# -*- coding:utf-8 -*-

import json
from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """根据指定国家，返回 pygal 使用的两字国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        elif name == 'Yemen, Rep':
            return 'ye'
        elif name == 'Arab World':
            return 'ab'
        elif name == 'Caribbean small states':
            return 'cl'
        elif name == 'East Asia & Pacific':
            return 'ep'
        elif name == 'European Union':
            return 'eu'
        elif name == 'Latin America & Caribbean':
            return 'lc'
    # 如果没有找到指定国家，返回 None
    return None

# print(get_country_code('Andorra'))
# print(get_country_code('China'))
# print(get_country_code('United Arab Emirates'))

# with open('population_data.json') as f:
#     countries = json.load(f)
#
# for country in countries:
#     country_name = country['Country Name']
#     code = get_country_code(country_name)
#     if code:
#         print(code + ' : ' + country_name)
#     else:
#         print('ERROR:' + country_name)