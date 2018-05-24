#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# crawling taobao MM photos

import os
import re
# import threading
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

browserPath = '/opt/chromedriver'
homePage = 'https://mm.taobao.com/search_tstar_model.htm?'
outputDir = 'photo/'
parser = 'html5lib'

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')


# phantomjs 已被废弃
# driver = webdriver.PhantomJS(executable_path=browserPath)


def main():
    driver = webdriver.chrome(executable_path=browserPath, chrome_options=chrome_options)
    driver.get(homePage)  # 访问目标网页
    bsObj = BeautifulSoup(driver.page_source, parser)  # 解析html代码
    print("[*]OK GET Page")
    # 获得主页上所有MM的姓名、所在城市、身高、体重等信息
    girlsList = driver.find_element_by_id('J_GirlsList').text.split('\n')
    # print(girlsList)
    # 获取所有MM封面图片
    imagesUrl = re.findall('\/\/gtd\.alicdn\.com\/sns_logo.*\.jpg', driver.page_source)
    # 获取个人主页地址等信息
    girlsUrl = bsObj.find_all(
        "a",
        {"href": re.compile("\/\/.*\.htm\?(userId=)\d*")})
    # 获取名字地点
    girlsNL = girlsList[::3]
    # 身高体重
    girlsHW = girlsList[1::3]
    # 个人主页地址
    girlsHURL = [('http:' + i['href']) for i in girlsUrl]
    # 封面照地址
    girlsPhotoURL = [('https:' + i) for i in imagesUrl]

    girlsInfo = zip(girlsNL, girlsHW, girlsHURL, girlsPhotoURL)

    # 姓名地址girlNL，身高体重girlHW，个人主页地址girlHRUL，封面图片URL
    for girlNL, girlHW, girlHURL, girlCover in girlsInfo:
        print("[*]Girl :", girlNL, girlHW)
        # 为妹子建立文件夹
        mkdir(outputDir + girlNL)
        print("    [*]saving...")
        # 获取妹子封面图片
        data = urlopen(girlCover).read()
        with open(outputDir + girlNL + '/cover.jpg', 'wb') as f:
            f.write(data)
        print("    [+]Loading Cover...")
        # 获取妹子个人主页中的图片
        getImgs(girlsHURL, outputDir + girlsNL)
    driver.close()


def mkdir(path):
    # 判断路径是否存在
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print("    [*]Created Folder", path)
        os.makedirs(path)
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print('    [*]Folder', path, 'already exists')


def getImgs(url, path):
    driver = webdriver.Chrome(executable_path=browserPath, chrome_options=chrome_options)
    driver.get(url)
    print("    [*]Opening...")
    bsObj = BeautifulSoup(driver.page_source, parser)
    # 获得模特个人页面上的艺术照地址
    imgs = bsObj.find_all("img", {"src": re.compile(".*\.jpg")})
    for i, img in enumerate(imgs[1:]):  # 不包含与封面图片一样的头像
        try:
            html = urlopen('https:' + img['src'])
            data = html.read()
            fileName = "{}/{}.jpg".format(path, i + 1)
            print(" [+]Loading...", fileName)
            with open(fileName, 'wb') as f:
                f.write(data)
        except Exception:
            print("    [!]Address Error!")
    driver.close()


if __name__ == '__main__':
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    main()
