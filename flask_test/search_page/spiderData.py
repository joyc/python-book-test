# coding:utf-8

import requests
import json
from lxml import etree


def search_info(keyword):
    results_list = []
    url = f'https://www.baidu.com/s?word={keyword}'
    print(f'----------{url}')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400'
    }

    response = requests.get(url, headers = headers)
    response.encoding = 'utf-8'

    # print(response.text)
    source = etree.HTML(response.text)
    results = source.xpath('//*[@id]/@data-tools')
    for r in results:
        try:
            str = json.loads(r.encode('utf-8'))
            results_list.append(str)
            print(str['title'], str['url'])
        except Exception as e:
            continue
    return results_list
