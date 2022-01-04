# 鸢尾花数据集：
import logging
import math

from sklearn import datasets


# 初始化数据
def get_dataset():
    # iris：鸢尾花数据集：--> 用于分类
    # 有150个数据集，共分为3类，每类50个样本。每个样本有4个特征。

    # 加载iris数据集
    iris = datasets.load_iris()

    # 打印数据集的相关信息
    n_samples, n_features = iris.data.shape
    # 输出：共有 150 个样本, 每个样本有 4 个特征
    logging.info("鸢尾花数据集,共有 {0} 个样本, 每个样本有 {1} 个特征，共分为 {2} 类 "
                 .format(n_samples, n_features, iris.target_names.shape[0]))

    print("0 = 山鸢尾(setosam),1 = 杂色鸢尾(versicolor),2 = 弗吉尼亚鸢尾(virginica)")

    # 给数据集划分训练集和测试集：
    from sklearn.model_selection import train_test_split  # 导入模块
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, train_size=120, random_state=22)
    show_dataset(x_train, y_train)

    return x_train, x_test, y_train, y_test


# 数据集展示
def show_dataset(x, y):
    name = ['花萼长度(cm)', '花萼宽度(cm)', '花瓣长度(cm)', '花瓣宽度(cm)', '类型']

    print('', end='\t')
    for item in name:
        print(item, end='\t')
    print()

    for i in range(len(x)):
        item = x[i]
        print(i, end=' \t\t')
        for num in item:
            print(num, end=' \t\t')
        print(y[i], end=' \t\t')
        print()


# 决策过程
def decision(data: list, p_cond, n_cond):
    p = []
    n = []
    k = []
    for i in range(len(data)):
        item = data[i]
        if p_cond(item[0]):
            p.append(item)
        elif n_cond(item[0]):
            n.append(item)
        else:
            k.append(item)

    return p, n, k
    # show_dataset(x_list, y_list)


# 信息熵
def entropy(mylist: list):
    setosam = 0
    versicolor = 0
    virginica = 0

    value = 0
    m = len(mylist)
    for item in mylist:
        if item[1] == 0:
            setosam += 1
        elif item[1] == 1:
            versicolor += 1
        else:
            virginica += 1

    value += (-1) * (setosam / m) * math.log2((setosam / m) + 1e-6)
    value += (-1) * (versicolor / m) * math.log2((versicolor / m) + 1e-6)
    value += (-1) * (virginica / m) * math.log2((virginica / m) + 1e-6)

    return value


# 信息增益
def gain(curr_set_entropy, p, n, k):
    m = len(p) + len(n) + len(k)
    child_set_etp = (len(p) / m) * entropy(p)
    child_set_etp += (len(n) / m) * entropy(n)
    child_set_etp += (len(k) / m) * entropy(k)
    return curr_set_entropy - child_set_etp


# 预测
def predict(data: list, actions):
    setosam = []
    versicolor = []
    virginica = []
    vv = []
    # 进行特征1的预测
    for item in data:
        if actions[3][0](item[0]):
            setosam.append(item)
        elif actions[3][1](item[0]):
            vv.append(item)
        else:
            virginica.append(item)
    # 进行特征2的预测
    for item in vv:
        if actions[2][0](item[0]):
            setosam.append(item)
        elif actions[2][1](item[0]):
            versicolor.append(item)
        else:
            virginica.append(item)

    acc_num = accuracy_num(setosam, 0) \
              + accuracy_num(versicolor, 1) \
              + accuracy_num(virginica, 2)
    print("测试集准确率为{:.2f}".format((acc_num / len(data)) * 100))


# 准确率分析
def accuracy_num(mylist: list, target: int):
    m = len(mylist)
    good = 0
    for item in mylist:
        if item[1] == target:
            good += 1
    return good


if __name__ == '__main__':
    x_train, x_test, y_train, y_test = get_dataset()

    print("训练集样本大小", x_train.shape)  # 输出：训练集样本大小 (120, 4)
    print("测试集样本大小", x_test.shape)  # 输出：训练集样本大小 (120, 4)

    actions = [(lambda x: x[0] < 5.3, lambda x: x[0] < 6.4)
        , (lambda x: x[1] > 3.3, lambda x: x[1] < 2.9)
        , (lambda x: x[2] < 2, lambda x: x[2] < 5)
        , (lambda x: x[3] < 1, lambda x: x[3] < 1.8)]

    # 全局分类
    data = [(y_train[i], y_train[i]) for i in range(len(y_train))]
    p, n, k = decision(data, lambda x: x == 0, lambda x: x == 1)
    curr_set_entropy = entropy(data)
    print("p={},n={},k={},信息熵 entropy={:.4f}".format(len(p), len(n), len(k), curr_set_entropy))

    # 第一个特征
    data = [(x_train[i], y_train[i]) for i in range(len(y_train))]
    p, n, k = decision(data, lambda x: x[0] < 5.3, lambda x: x[0] < 6.4)
    gain_1 = gain(curr_set_entropy, p, n, k)
    print("特征1：p={},n={},k={},信息增益 gain={:.4f}".format(len(p), len(n), len(k), gain_1))

    # 第二个特征
    p, n, k = decision(data, lambda x: x[1] > 3.3, lambda x: x[1] < 2.9)
    gain_2 = gain(curr_set_entropy, p, n, k)
    print("特征2：p={},n={},k={},信息增益 gain={:.4f}".format(len(p), len(n), len(k), gain_2))

    # 第三个特征
    p, n, k = decision(data, lambda x: x[2] < 2, lambda x: x[2] < 5)
    gain_3 = gain(curr_set_entropy, p, n, k)
    print("特征3：p={},n={},k={},信息增益 gain={:.4f}".format(len(p), len(n), len(k), gain_3))

    # 第四个特征
    p, n, k = decision(data, lambda x: x[3] < 1, lambda x: x[3] < 1.8)
    gain_4 = gain(curr_set_entropy, p, n, k)
    print("特征4：p={},n={},k={},信息增益 gain={:.4f}".format(len(p), len(n), len(k), gain_4))

    data = [(x_test[i], y_test[i]) for i in range(len(y_test))]
    predict(data, actions)
