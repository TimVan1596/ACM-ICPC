# -*- coding:utf-8 -*-
# @Time:2020/8/5 1:40
# @Author:TimVan
# @File:testUrllib.py
# @Software:PyCharm

import urllib.request

# baseUrl = "https://www.timvanx.com/"
#
# # get方式请求
# response = urllib.request.urlopen(baseUrl)
# # 对获取到的网页源码进行utf-8解码
# print(response.read().decode("utf-8"))

# post方式请求
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"id": 2}), encoding="utf-8")
# postBaseUrl = "https://www.timvanx.com/php/getnewsitem.php"
# # 超时处理
# try:
#     response = urllib.request.urlopen(postBaseUrl
#                                       , data=data
#                                       ,timeout=0.01)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("结果超时:{0}".format(e))


# import urllib.parse
# data = bytes(urllib.parse.urlencode({"id": 2}), encoding="utf-8")
# # postBaseUrl = "https://www.timvanx.com/php/getnewsitem.php"
# postBaseUrl = "https://www.baidu.com"
# response = urllib.request.urlopen(postBaseUrl
#                                   , data=data
#                                   ,timeout=30)
# print(response.read().decode("utf-8"))
# print(response.status)
# print(response.getheaders())
# print(response.getheader("Server"))

# 对豆瓣进行爬取
import urllib.parse

douBanUrl = "https://www.douban.com"
# User-Agent:
# Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
data = bytes(urllib.parse.urlencode({"id": 2}), encoding="utf-8")
req = urllib.request.Request(url=douBanUrl
                             # , data=data
                             , headers=headers
                             # , method="post"
                             )
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
