# -*- coding:utf-8 -*-
# @Time:2020/8/7 17:37
# @Author:TimVan
# @File:testBs4.py
# @Software:PyCharm

# from bs4 import BeautifulSoup
#
# file = open("./baidu.html", "rb")
# html = file.read()
# bs = BeautifulSoup(html, "html.parser")

# 1、Tag，标签
# print(bs.title)
# print(bs.head)
# print(bs.a)
# print(type(bs.head))


# 2、NavigableString，简单理解为标签中的内容，即字符串
# res = bs.title.string
# print(bs.title.string)
# print(type(res))

# res = bs.a.attrs
# print(res)
# print(type(res))

# 3、BeautifulSoap，整个文档
# res = bs
# print(res)
# print(type(res))

# 4、Comment 注释类型
# res = bs.a.string
# print(res)
# print(type(res))


from bs4 import BeautifulSoup

file = open("./baidu.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")

# 对文档进行遍历
# res = bs.head.contents
# print(res)
# print(type(res))
# print(res[1])

# 对文档进行搜索

# ① find_all()
# 字符串过滤
# res = bs.find_all("a")
# print(res)
# 正则表达式
# import re
# res = bs.find_all(re.compile("a"))
# print(res)
# 方法，传入函数进行判断
# def is_exist_class(tag):
#     # has_attr 返回true or false
#     return tag.has_attr("class")
#
# # 注意内容可重复（交叉）
# res = bs.find_all(is_exist_class)
# print(res)
# key word args 参数
# res = bs.find_all(id="s-top-left")
# for item in res:
#     print(item)
# res = bs.find_all(class_="carbon-text")
# for item in res:
#     print(item)
# 存在content
# res = bs.find_all(content=True)
# for item in res:
#     print(item)

# 文本参数
import re

# res = bs.find_all(text=['地图', '贴吧'])
# 正则表达式
# res = bs.find_all(text=re.compile('\d'))
# for item in res:
#     print(item)

# limit，取多少个
# res = bs.find_all('a',limit=3)
# for item in res:
#     print(item)

# css选择器
# res = bs.select('.carbon-text')
# res = bs.select('#tieba')
# res = bs.select('a[class="carbon-text"]')
res = bs.select('div>a')
for item in res:
    print(item)
