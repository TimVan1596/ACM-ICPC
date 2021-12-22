import numpy as np
import math


# 将数据集切分成t份，便于实现mini-batch(先打乱，再拆分)
# x = 数据集，y=对应的结果
def split_data(x, y, t=1):
    # 首先判断x和y的长度是否匹配
    assert x.shape[1] == y.shape[1]
    m = x.shape[1]

    state = np.random.get_state()
    np.random.shuffle(x.T)
    np.random.set_state(state)
    np.random.shuffle(y.T)

    x_list = []
    y_list = []
    max_k = math.ceil(x.shape[1] / t)
    for i in range(max_k):
        start = i * t
        end = start + t if (start + t) <= m else None
        x_list.append(x[:, start:end])
        y_list.append(y[:, start:end])
    return x_list, y_list


# mini-batch梯度下降法
def random_mini_batches(X, Y, mini_batch_size=64, seed=0):
    """
    从（X，Y）中创建一个随机的mini-batch列表

    参数：
        X - 输入数据，维度为(输入节点数量，样本的数量)
        Y - 对应的是X的标签，【1 | 0】（蓝|红），维度为(1,样本的数量)
        mini_batch_size - 每个mini-batch的样本数量

    返回：
        mini-bacthes - 一个同步列表，维度为（mini_batch_X,mini_batch_Y）

    """

    np.random.seed(seed)  # 指定随机种子
    m = X.shape[1]
    mini_batches = []

    # 第一步：打乱顺序
    # 它会返回一个长度为m的随机数组，且里面的数是0到m-1
    permutation = list(np.random.permutation(m))
    # 将每一列的数据按permutation的顺序来重新排列。
    shuffled_X = X[:, permutation]
    shuffled_Y = Y[:, permutation].reshape((1, m))

    """
    #博主注：
    #如果你不好理解的话请看一下下面的伪代码，看看X和Y是如何根据permutation来打乱顺序的。
    x = np.array([[1,2,3,4,5,6,7,8,9],
				  [9,8,7,6,5,4,3,2,1]])
    y = np.array([[1,0,1,0,1,0,1,0,1]])

    random_mini_batches(x,y)
    permutation= [7, 2, 1, 4, 8, 6, 3, 0, 5]
    shuffled_X= [[8 3 2 5 9 7 4 1 6]
                 [2 7 8 5 1 3 6 9 4]]
    shuffled_Y= [[0 1 0 1 1 1 0 1 0]]
    """

    # 第二步，分割
    num_complete_minibatches = math.floor(m / mini_batch_size)  # 把你的训练集分割成多少份,请注意，如果值是99.99，那么返回值是99，剩下的0.99会被舍弃
    for k in range(0, num_complete_minibatches):
        mini_batch_X = shuffled_X[:, k * mini_batch_size:(k + 1) * mini_batch_size]
        mini_batch_Y = shuffled_Y[:, k * mini_batch_size:(k + 1) * mini_batch_size]
        """
        #博主注：
        #如果你不好理解的话请单独执行下面的代码，它可以帮你理解一些。
        a = np.array([[1,2,3,4,5,6,7,8,9],
                      [9,8,7,6,5,4,3,2,1],
                      [1,2,3,4,5,6,7,8,9]])
        k=1
        mini_batch_size=3
        print(a[:,1*3:(1+1)*3]) #从第4列到第6列
        '''
        [[4 5 6]
         [6 5 4]
         [4 5 6]]
        '''
        k=2
        print(a[:,2*3:(2+1)*3]) #从第7列到第9列
        '''
        [[7 8 9]
         [3 2 1]
         [7 8 9]]
        '''

        #看一下每一列的数据你可能就会好理解一些
        """
        mini_batch = (mini_batch_X, mini_batch_Y)
        mini_batches.append(mini_batch)

    # 如果训练集的大小刚好是mini_batch_size的整数倍，那么这里已经处理完了
    # 如果训练集的大小不是mini_batch_size的整数倍，那么最后肯定会剩下一些，我们要把它处理了
    if m % mini_batch_size != 0:
        # 获取最后剩余的部分
        mini_batch_X = shuffled_X[:, mini_batch_size * num_complete_minibatches:]
        mini_batch_Y = shuffled_Y[:, mini_batch_size * num_complete_minibatches:]

        mini_batch = (mini_batch_X, mini_batch_Y)
        mini_batches.append(mini_batch)

    return mini_batches


if __name__ == '__main__':
    x = np.linspace(1, 10, 10, dtype='int').reshape(2, 5)
    y = np.array([x[0, i] + x[1, i] for i in range(len(x[0,]))]).reshape(1, -1)
    print(x)
    print(y)
    dataset = (x, y)

    # 切分成每单位2个
    x_list, y_list = split_data(x, y, t=2)
    print(x_list)
    print(y_list)

    mini_batches = random_mini_batches(x, y, mini_batch_size=2, seed=0)
    print(mini_batches)
