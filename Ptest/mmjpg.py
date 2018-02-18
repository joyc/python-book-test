#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
抓取 http://www.mmjpg.com/ 排行榜的图片，直接就可以抓取
'''
import os
import requests
from bs4 import BeautifulSoup as bs

url = "http://www.mmjpg.com/hot/" # 目标网址
url_a = "http://www.mmjpg.com"  # 下一页的网址中固定的部分

# 请求头，习惯性的添加了，可以没有
headers = {
    "Connection":"keep-alive",
    "Host":"www.mmjpg.com",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}

# 又是个请求头，这个必须要有，因为目标站点有防外链的设定
headers1 = {
    "Connection":"keep-alive",
    "Host":"img.mmjpg.com",
    "Referer":"http://www.mmjpg.com/mm/1013/5",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}

# 获取页面url
def get_page_url(url):

    rep = requests.get(url,headers = headers)
    rep.encoding="utf_8"
    soup = bs(rep.text,"html.parser")
    page_url = soup.select('.pic ul li[class="like"] a')

    for x in page_url:
        yield {
            "title":x["title"],
            "page_url":x["href"]
        }

# 下载器
def downloader(url,title,n):
    rep = requests.get(url,headers = headers1)
    print(rep.status_code)
        # 创建下载目录，如果目录存在就不创建
    if not os.path.exists("%s" % title):
        os.mkdir("%s" % title)
        #因为目标站点的服务器有一点问题，好多图片一次是打不开的，
        #需要刷新好几次，这里就是让下载器在获取到图片之前对一张
        #图片最多刷新6次
    t = 0
    while t < 6:
        if  rep.status_code == 200:
            with open("%s/%s.jpg" % (title,n),"wb") as f:
                print("%s.jpg开始下载" % n)
                f.write(rep.content)
                print("%s.jpg下载完成 \n" % n)
            break
        else:
            rep = requests.get(url,headers = headers1)
            t = t + 1
            continue
    return n+1

# 获取图片的地址
def get_image_url(url,title,m):
    n = m
    rep = requests.get(url,headers = headers)
    print(url)
    rep.encoding="utf_8"
    soup = bs(rep.text,"html.parser")
    print(title)

    image_url = soup.select(".article .content a img")[0]["src"]
    if soup.select('.article .page [class="ch next"]')[0].get_text() == "下一张" :
        next_page = url_a + soup.select('.article .page [class="ch next"]')[0]["href"]
        print(next_page)
        n = downloader(image_url,title,n)
        get_image_url(next_page,title,n)  # 递归
    else:
        return

def main():
    for x in get_page_url(url):
        get_image_url(x["page_url"],x["title"],1)

if __name__ == '__main__':
    main()
