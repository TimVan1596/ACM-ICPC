# -*- coding: UTF-8 -*-
# helloworld.py
import math
import time


def get_unix_time(dt):
    # 转换成时间数组
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = time.mktime(timeArray)
    return timestamp


def fun(x):
    return 3E-10 * math.pow(x, 3) - 6E-04 * x + 1.106


if __name__ == '__main__':
    time_now = '2022-04-18 08:33:20'
    unix = get_unix_time(dt=time_now) - 1650000000
    ret = fun(unix)
