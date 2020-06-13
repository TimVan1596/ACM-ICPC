# -*- coding:utf-8 -*-
# @Time:2020/6/4 11:10
# @Author:TimVan
# @File:8个老师随机分配到3个办公室.py
# @Software:PyCharm
import random

offices = [[], [], []]
teacherList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
i = 0
for teacher in teacherList:
    officeIndex = random.randint(0, 2)
    offices[officeIndex].extend(teacher)

print("offices=>")
for i in range(len(offices)):
    print(offices[i], end="\t")
print()
