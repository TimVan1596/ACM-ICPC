# 鸢尾花数据集：
from sklearn import datasets

if __name__ == '__main__':
    # iris：鸢尾花数据集：--> 用于分类
    # 有150个数据集，共分为3类，每类50个样本。每个样本有4个特征。

    # 加载数据集
    iris = datasets.load_iris()  # 加载iris数据集

    # 打印数据集的相关信息
    n_samples, n_features = iris.data.shape
    print("鸢尾花数据集,共有", n_samples, "个样本, 每个样本有", n_features, "个特征")  # 输出：共有 150 个样本, 每个样本有 4 个特征

    # 给数据集划分训练集和测试集：
    from sklearn.model_selection import train_test_split  # 导入模块

    x_train, x_test, y_train, t_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)
    print("训练集样本大小", x_train.shape)  # 输出：训练集样本大小 (120, 4)
    print("训练集标签大小", y_train.shape)  # 输出：训练集标签大小 (120,)
    name = ['花萼长度(cm)', '花萼宽度(cm)', '花瓣长度(cm)', '花瓣宽度(cm)']

    print('', end='\t')
    for item in name:
        print(item, end='\t')
    print()

    for i in range(len(x_train)):
        item = x_train[i]
        print(i, end='  \t\t')
        for num in item:
            print(num, end='  \t\t')
        print()
