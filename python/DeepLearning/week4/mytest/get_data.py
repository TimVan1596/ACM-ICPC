# 用于获取数据
import random
import math


# 获得数据
# num = 样本数量
def get_number(num):
    X = [
        [],
        [],
        []
    ]
    Y = []
    i = 0
    for i in range(num):
        x = random.randint(0, 50)
        y = random.randint(0, 100)
        z = random.randint(0, 100)
        temp = math.pow(x, 2) + y - 6 * z
        result = 1
        if temp < 0:
            result = 0
        X[0].append(x)
        X[1].append(y)
        X[2].append(z)
        Y.append(result)
        # print("-- 当 i =" + str(i))
        # print("x=" + str(x))
        # print("y=" + str(y))
        # print("z=" + str(z))
        # print("temp=" + str(temp))
        # print("result=" + str(result))
        # print("-" * 10)
    return X, Y


if __name__ == '__main__':
    X, Y = get_number(10)
    print(X)
    print(Y)
