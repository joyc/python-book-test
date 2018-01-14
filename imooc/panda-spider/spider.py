#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/15/0015 0:21
# @Author  : Hython.com
# @File    : spider.py.py
import re
from urllib import request

import sys, io

# 改变标准输出的默认编码
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


class Spider():
    url = 'https://www.panda.tv/cate/acg'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)
        # print(anchors[0])
        return anchors

    def __refine(self, anchors):
        l = lambda anchor: {
            'name': anchor['name'][0].strip(),
            'number': anchor['number'][0]
        }
        return map(l, anchors)

    def __sort(self, anchors):
        # filter
        anchors = sorted(anchors, key=self.__sort__seed, reverse=True)
        return anchors

    def __sort__seed(self, anchor):
        r = re.findall('\d*', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __show(self, anchors):
        for rank in range(len(anchors)):
            print('rank ' + str(rank + 1)
                  + '  : ' + anchors[rank]['name']
                  + '    ' + anchors[rank]['number'] + '人')

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        # print(anchors)
        self.__show(anchors)


spider = Spider()
spider.go()