# -*- coding:utf-8 -*-
# @Time:2020/6/4 15:43
# @Author:TimVan
# @File:商品购物车.py
# @Software:PyCharm

# 现有商品列表如下：
# 1. products = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],
# ["Nike",699]]，需打印出以下格式：
# ------  商品列表 ------
# 0  iphone   6888
# 1  MacPro   14800
# 2  小米6    2499
# 3  Coffee   31
# 4  Book    60
# 5  Nike    699
# 2. 根据上面的products列表写一个循环，不断询问用户想买什么，用户选择一个商品编号，就把对应
# 的商品添加到购物车里，最终用户输入q退出时，打印购买的商品列表。

# 商品清单
products = [["iphone", 6888], ["MacPro", 14800], ["小米6", 2499]
    , ["Coffee", 31], ["Book", 60], ["Nike", 699]]
# 购物车列表
cart = []

command = "no q"
EXIT = "q"

while command != EXIT:
    # 展示商品列表
    print("-" * 6, "  商品列表  ", "-" * 6)
    i = 0
    length = len(products)
    for i in range(length):
        good = products[i]
        print("%d\t%s\t%d" % (i, good[0], good[1]))
    # 输入
    command = input("请输入您想要购买商品的编号\n")
    if command != EXIT:
        if command.isdigit():
            index = int(command)
            if index < length:
                cart.append(products[index])
                print("已加入购物车")
            else:
                print("未找到这个编号")
        else:
            print("您输入的不是数字")

# 展示购物车
print("-" * 6, "  购物车  ", "-" * 6)
i = 0
length = len(cart)
totalPrice = 0
for i in range(length):
    good = cart[i]
    print("%d\t%s\t%d" % (i, good[0], good[1]))
    totalPrice += good[1]
print("共 %d 件，合计总价为 %d 元" % (length, totalPrice))
