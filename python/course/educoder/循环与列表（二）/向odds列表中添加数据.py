

def EnLevel(n):
    # 请在这里编写程序，完成本关任务
    #   请在此添加实现代码   #
    # ********** Begin *********#
    import math
    me = 9.1094e-31
    e = 1.6022e-19
    e0 = 8.8542e-12
    h = 6.6261e-34
    En = (me * math.pow(e, 4)) / (8 * math.pow(e0, 2) * math.pow(h, 2))
    En = -En
    print("{:.5e}".format(En))
    return En
# ********** End **********#

level = int(1)
EnLevel(level)