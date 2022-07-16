def Table_For(min, max):
    # 请在此处用for循环打印列表
    #   请在此添加实现代码   #
    # ********** Begin *********#
    print("华氏度\t\t摄氏度\t\t近似摄氏度")
    print("****************************************")
    for f in range(min, max + 1, 10):
        c = (f - 30) / 2
        c_auccracy = (f - 32) / 1.8
        print("{0}\t\t{1:.1f}\t\t{2}".format(f, c_auccracy, c))


# ********** End **********#

def Table_While(min, max):
    # 请在处用while循环打印列表
    #   请在此添加实现代码   #
    # ********** Begin *********#
    print("华氏度\t\t摄氏度\t\t近似摄氏度")
    print("****************************************")
    f = min
    while f < max + 1:
        c = (f - 30) / 2
        c_auccracy = (f - 32) / 1.8
        print("{0}\t\t{1:.1f}\t\t{2}".format(f, c_auccracy, c))
        f += 10


# ********** End **********#

min = int(0)
max = int(30)
Table_For(min, max)
Table_While(min, max)
