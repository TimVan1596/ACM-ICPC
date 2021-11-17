
# coding:utf-8


Lst = '1,-2, 6, 11, -5'
Lst = Lst.split(',')

def abs_sum(L):
#请在此添加代码，以递归的方式设计函数abs_sum(L)返回列表L（假设其中全是整数）中所有整数绝对值之和
#********** Begin *********#
    if len(L) <= 0:
        return 0
    import math
    temp = abs(int(L.pop()))
    total = 0
    total = temp + abs_sum(L)
    return total


#**********  End  *********#

print(abs_sum(Lst))
