# -*- coding:utf-8 -*-
# @Time:2020/9/1 11:33
# @Author:TimVan
# @File:main.py
# @Software:PyCharm
import random
from typing import Tuple

LEARNING_RATE = 0.00001
ROUND_MAX = 20000


# 读取数据
def readData(src: str) -> list:
    dataList = []
    f = open(src)  # 返回一个文件对象
    line = f.readline()  # 调用文件的 readline()方法
    while line:
        # print(line, end='')  # 在 Python 3中使用
        data = line.strip().split(',')
        dataList.append(data)
        line = f.readline()
    f.close()
    return dataList


# 计算loss函数
def getLoss(w: float, b: float, dataList: list) -> float:
    lossValue = 0.0
    for data in dataList:
        x = float(data[0])
        y = float(data[1])
        lossValue += (w * x + b - y) ** 2
    # 总值除以个数
    lossValue /= len(dataList)
    return lossValue


# 计算loss对w和b的偏导
def getDerivativeWandB(w: float, b: float, dataList: list) -> Tuple[float, float]:
    # 对w和b的偏导值
    wDeri = 0.0
    bDeri = 0.0
    for data in dataList:
        x = float(data[0])
        y = float(data[1])
        wDeri += (w * x + b - y) * x
        bDeri += (w * x + b - y)
    # 总值除以个数
    wDeri = (2 * wDeri) / len(dataList)
    bDeri = (2 * bDeri) / len(dataList)
    return wDeri, bDeri


if __name__ == '__main__':
    # 思路：
    # 1、读取数据，列表，列表的每个元素是一个元组，元组格式是(x0,y0)的形式
    # 2、计算当前loss函数
    # 3、生成随机的w和b值（默认为0和0）,指定一个learning rate值
    # 4、计算loss对w的偏导，和loss对b的偏导(w' = w - lr*偏导)
    # 5、循环4的步骤
    # 6、输出新的loss

    # 设计：
    # 1、计算loss函数：getLoss(w:float,b:float,dataList:list)->float
    # 2、计算loss对w的偏导：getDerivativeW(w:float,b:float,dataList:list)->float
    # 3、计算loss对b的偏导：getDerivativeW(w:float,b:float,dataList:list,learningRate:float)->float
    # 4、读取数据：readData(src:str)->list
    # 5、① main中首先读取数据，指定w、b、learningRate、循环次数的值，计算loss函数值
    #    ② 进入循环体，计算偏导并更新w和b
    #    ③ 结束循环，并计算新的loss函数值

    # main中首先读取数据
    dataSrc = "data.csv"
    dataList = readData(dataSrc)

    # 指定w、b、learningRate、循环次数的值
    w = random.randint(0, 9)
    b = random.randint(0, 9)
    learningRate = LEARNING_RATE
    roundMax = ROUND_MAX

    # 计算loss函数值
    lossValue = getLoss(w, b, dataList)
    print("-" * 15 + "\n"
          , "在w={0}，b={1}下，lossValue={2}".format(w, b, lossValue)
          , "\n" + "-" * 15)

    # 进入循环体，计算偏导并更新w和b
    for i in range(roundMax):
        wDeri, bDeri = getDerivativeWandB(w, b, dataList)
        w = w - learningRate * wDeri
        b = b - learningRate * bDeri

    # 计算loss函数值
    lossValue = getLoss(w, b, dataList)
    print("-" * 15 + "\n"
          , "在w={0}，b={1}下，lossValue={2}".format(w, b, lossValue)
          , "\n" + "-" * 15)
