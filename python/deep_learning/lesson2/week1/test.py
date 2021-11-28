import numpy as np


# 对传入数据进行归一化处理
# data的shape应该是(x,m)，其中x是特征值的个数，m是样本数量
# 返回归一化结果、u和delta_double
def normalizing(data: np.ndarray):
    # m = 样本数量
    m = data.shape[1]
    # 1.零均值：对每一个特征值分别求均值
    u = (1 / m) * data.sum(axis=1, keepdims=True)
    cache = data - u

    # 2.归一化方差：注意，是先平方再求和，这是为了避免如[-1,0,1]数据造成求和为0，之后产生除以0
    delta_double = (1 / m) * (cache ** 2).sum(axis=1, keepdims=True)
    cache = cache / delta_double
    return cache, u, delta_double


# 已知u和delta_double进行归一化输入
def normalizing_full(data: np.ndarray, u, delta_double):
    assert data.shape[0] == u.shape[0]
    assert data.shape[0] == delta_double.shape[0]

    cache = data - u
    cache = cache / delta_double
    return cache, u, delta_double


if __name__ == '__main__':
    # 输入的数组 shape=(2,3)
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    new_arr, u, delta_double = normalizing(data=arr)
    print(new_arr, u, delta_double)

    new_arr, u, delta_double = normalizing_full(data=arr, u=u, delta_double=delta_double)
    print(new_arr, u, delta_double)
