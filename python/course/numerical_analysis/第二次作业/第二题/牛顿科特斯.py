import math

aa = float(15565 / 2)
C = float(1945 / 2)

def f(x):
    value = 1 - ((C / aa) * math.sin(x)) ** 2
    return math.sqrt(value)


if __name__ == '__main__':
    a = 0
    b = 0.5 * math.pi
    # h = 步长
    h = (b - a) / 4
    # Cotes系数
    factor = [7, 30, 12, 32, 7]
    Cotes = 0
    # Cotes求积公式：[a,b]区间5节点4等距
    for k in range(5):
        x = a + k * h
        Cotes += factor[k] * f(x)
    Cotes *= ((b - a) / 90)
    S = Cotes * aa
    print("Cotes={}".format(Cotes))
    print("Cotes积分计算周长={}".format(S))

