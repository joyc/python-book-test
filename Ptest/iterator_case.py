#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/17/0017 23:13
# @Author  : Hython.com
# @File    : iterator_case.py
import requests
from collections import Iterable, Iterator

# def getWeather(city):
#     r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
#     data = r.json()['data']['forecast'][0]
#     return '%s: %s , %s ' % (city, data['low'], data['high'])

# u'北京', u'上海', u'广州', u'河北'
# print(getWeather('深圳'))
# print(getWeather('北京'))
# print(getWeather('昆明'))


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s: %s , %s ' % (city, data['low'], data['high'])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


for x in WeatherIterable(['北京', '上海', '广州', '河北', '昆明', '厦门', '柳州', '张家口']):
    print(x)