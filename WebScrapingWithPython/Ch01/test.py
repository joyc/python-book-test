#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib2
import re

def download(url, num_retries=2):
    print 'Downloading:', url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Downloading error:', e.reason
        html = None
        if num_retries > 0:
            # recursively retry 5xx HTTP errors
            return download(url, num_retries-1)
    return html


def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url)
    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # download each link
    for link in links:
        html = download(link)
        # scrape html here


if __name__ == '__main__':
    #download('http://httpstat.us/500')
    crawl_sitemap('http://example.webscraping.com/sitemap.xml')
