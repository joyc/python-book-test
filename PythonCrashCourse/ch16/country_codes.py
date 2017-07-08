#! python3
# -*- coding:utf-8 -*-

from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """根据指定国家，返回 pygal 使用的两字国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # 如果没有找到指定国家，返回 None
    return None

# print(get_country_code('Andorra'))
# print(get_country_code('China'))
# print(get_country_code('United Arab Emirates'))