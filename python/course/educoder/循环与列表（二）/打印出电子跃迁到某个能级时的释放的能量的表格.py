def EnList(maxn):
    # 请在这里编写程序，打印跃迁能量表
    # 请在右侧编辑器的EnList函数中，打印出电子跃迁到某个能级时的释放的能量的表格。
    #
    # 这个函数有一个参数maxn，代表要输出的行数，范围为1 - 20 。
    #
    # 表格总共5列，从左至右依次代表电子的起始能级1 - 5 。
    # 表格的每一行代表不同起始能级的电子跃迁到此能级所释放的能量。
    # 表格从能级1开始。
    #
    # 注意：需要打印表头，以及控制表格格式，具体要求请见测试说明。
    #
    # 输入数据由评测系统负责读取并传递给EnList函数，学生只需要关注这个函数的实现。
    import math
    me = 9.1094e-31
    e = 1.6022e-19
    e0 = 8.8542e-12
    h = 6.6261e-34
    print("  |能级1\t\t能级2\t\t能级3\t\t能级4\t\t能级5")
    print("--------------------------------------------------------------------------------")
    for i in range(1, maxn + 1):
        print("{} | ".format(i), end="")
        for j in range(1, 6):
            En = (me * math.pow(e, 4)) / (8 * math.pow(e0, 2) * math.pow(h, 2))
            En = En * (1 / math.pow(i, 2) - 1 / math.pow(j, 2))
            if En == 0:
                En = -En
            print("{:.6E}\t".format(En), end="")
        print()


if __name__ == "__main__":
    maxn = int(3)
    EnList(maxn)
