# 请用函数实现Machin公式计算，包含隐含参数N
import math


def arctg(x, N=5):  # 迭代项数N的缺省值是5，即如果调用时不给值就用5
    # ********** Begin *********#
    # 为了使用Machin方法更快的计算出π值，请在右侧代码框中编写程序实现arctg函数，根据输入的x和迭代项数N返回相应的arctg值。
    sum = 0
    for i in range(1, N + 1):
        value = math.pow(-1, i - 1)
        value = value * ((math.pow(x, 2 * i - 1)) / (2 * i - 1))
        sum = sum + value
    # ********** End **********#
    return sum

print('%.20f' % arctg(float(0.1)))
