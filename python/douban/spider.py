# -*- coding:utf-8 -*-
# @Time:2020/8/4 11:55
# @Author:TimVan
# @File:spider.py
# @Software:PyCharm


import urllib.request, urllib.error  # urllib:制定URL，获取网页数据
from bs4 import BeautifulSoup  # bs4：网页解析，获取数据
import re  # re：正则表达式，进行文字匹配
import xlwt  # xlwt：进行excel操作
import sqlite3  # sqlite3:进行SQLite数据库操作


def main():
    # 1.爬取网页
    # 2.逐一解析数据
    # 3.保存数据(SQL或Excel)
    baseUrl = "https://movie.douban.com/top250?start="
    savePath = ".\\豆瓣电影TOP250.xls"

    getData(baseUrl)
    saveData(savePath)


# 读取一个URL，并返回其源码
def askUrl(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=header)
    # html=待返回源码
    html = None
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        print("请求错误")
        if hasattr(e, "code"):
            print("，错误状态码为{}".format(e.code))
        if hasattr(e, "reason"):
            print("，原因为{}".format(e.reason))
    return html


# 1.爬取网页
def getData(baseUrl):
    dataList = []

    html = askUrl(baseUrl)
    print(html)

    # 2.逐一解析数据
    return dataList


# 3.保存数据(SQL或Excel)
def saveData(savePath):
    print()


if __name__ == "__main__":
    main()
