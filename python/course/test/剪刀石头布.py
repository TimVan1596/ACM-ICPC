# -*- coding:utf-8 -*-
# @Time:2020/6/2 11:47
# @Author:TimVan
# @File:剪刀石头布.py
# @Software:PyCharm

import random

action = input("请输入剪刀(0)、石头(1)、布(2):\n")
# 检查是否输入数字
if int(action) < 0 or int(action) > 2:
    print("输入范围有误")
else:
    action = int(action)

    print("您出的是", end='')
    if action == 0:
        print("剪刀")
    elif action == 1:
        print("石头")
    elif action == 2:
        print("布")
    else:
        print("错误指令")

    enemy = random.randint(0, 2)
    print("对方出的是", end='')
    if enemy == 0:
        print("剪刀")
    elif enemy == 1:
        print("石头")
    elif enemy == 2:
        print("布")
    else:
        print("错误指令")

    if action - enemy == 1 or action - enemy == -2:
        print("胜利")
    elif action - enemy == 0:
        print("平手")
    else:
        print("失败")
