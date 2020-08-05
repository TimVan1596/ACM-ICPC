# -*- coding:utf-8 -*-
# @Time:2020/8/5 1:40
# @Author:TimVan
# @File:testUrllib.py
# @Software:PyCharm

import urllib.request

baseUrl = "https://www.timvanx.com/"
response = urllib.request.urlopen(baseUrl)
print(response.read().decode("gbk"))