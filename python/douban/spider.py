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

# 1.爬取网页
def getData(baseUrl):
    dataList = []
    # 2.逐一解析数据
    return dataList


# 3.保存数据(SQL或Excel)
def saveData(savePath):
    print()

if __name__ == "__main__":
    main()
