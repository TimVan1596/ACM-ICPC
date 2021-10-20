import math
import random


# 获得正常数据（Y的非负概率基本为0.5）
# num = 需要的样本数量
# X_shape = X的特征数
def get_normal_data(num, X_shape=5):
    X = []
    for index in range(X_shape):
        X.append([])
    Y = []
    i = 0
    for i in range(num):
        temp = 0
        for index in range(X_shape):
            elem = random.randint(-200, 200)
            if index % 2 == 0:
                temp += math.sin(elem)
            else:
                temp += math.cos(elem)
            X[index].append(elem)
        result = 1
        if temp <= 0:
            result = 0
        Y.append(result)

    return X, Y


# 获得一个list中的非负数的个数
def get_positive_num(my_list):
    num = 0
    for number in my_list:
        if number > 0:
            num += 1
    return num


if __name__ == '__main__':
    X, Y = get_normal_data(100000)
    print(X)
    print(Y)
    print('正数率为 ' + str(get_positive_num(Y) / len(Y)))
