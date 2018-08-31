#!/usr/bin/env python
# coding=utf-8
# 网页下载器
import urllib.request


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        response =urllib.request.urlopen(url)
        # code不为200则请求失败
        if response.getcode() != 200:
            return None
        return response.read()
