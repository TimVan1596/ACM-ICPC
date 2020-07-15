# -*- coding:utf-8 -*-
# @Time:2020/7/15 14:33
# @Author:TimVan
# @File:tool.py
# @Software:PyCharm
# 作为一个tool模块

def printName():
    # print("its:%s"% __name__)
    return __name__

def add(a: int, b: int) -> int:
    return a + b
