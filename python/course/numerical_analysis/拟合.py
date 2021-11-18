import numpy
from matplotlib import pyplot as plt
import numpy as np
import math


# 将字符串按空格转list
def str_to_list(str):
    cache = str.split()
    if '.' in str:
        return [float(elem) for elem in cache]
    else:
        return [int(elem) for elem in cache]


# 获取数据
def get_data(t_str, P_str):
    t = str_to_list(t_str)
    P = str_to_list(P_str)
    return t, P


# 初始化matplotlib.pyplot
# y是真实值的list，f是拟合后的list
def initial_plt(x, y, f, fx_ln=[], fx_label='二次拟合', ln_fx_label='对数函数', is_show=True):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.xlabel('t/min 时间')
    plt.ylabel('P 所占产物的百分比')
    plt.title('最小平方和拟合')

    plt.scatter(x, y, linewidth=2, color='orange', label='真实')
    plt.plot(x, f, linewidth=2, color='dodgerblue', label=fx_label)
    plt.plot(x, fx_ln, linewidth=2, color='green', label=ln_fx_label)

    plt.legend(loc='upper left')
    if is_show:
        plt.show()
    plt.savefig("result.png")


# 计算phi的值的方法
# phi_fun是一个函数
def get_phi(x, phi_fun):
    return [phi_fun(xx) for xx in x]


# 获得phi的真实值
def get_phi_value(t, phi):
    phi_values = []
    # 初始化phi列表
    for phi_fun in phi:
        phi_list = get_phi(t, phi_fun)
        phi_values.append(phi_list)
    return phi_values


# 获得G矩阵
def get_G(phi_values) -> list:
    shape = len(phi_values)
    # print("维度为" + str(shape))
    G = np.zeros((shape, shape), dtype=float)

    for i in range(0, shape):
        for j in range(0, shape):
            value = 0
            if i > j:
                value = G[j, i]
            else:
                value = elem_wise(phi_values[i], phi_values[j])
            G[i, j] = value
    # phi_values.append(value)
    # print(phi_values[0])
    return G.tolist()


# 获得d矩阵
def get_d(phi_value, y) -> list:
    shape = len(phi_value)
    # 构造d行矩阵
    d = []
    for i in range(shape):
        value = elem_wise(phi_value[i], y)
        d.append(value)
    return d


# 内积
def elem_wise(a: list, b: list):
    # 做内积必然对应项相同
    assert len(a) == len(b)
    new_list = list(map(lambda tup: tup[0] * tup[1], zip(a, b)))
    return sum(new_list)


# 格式化数字
def format_num(num, m_type) -> str:
    return "{0:12}".format(m_type(num))


# 打印list型的矩阵
def print_list(mylist, name='list'):
    print("{0}=".format(name))
    for line in mylist:
        print('[', end='')
        if type(line) == list:
            for elem in line:
                print(format_num(elem, type(elem)), end='')
        else:
            print(format_num(line, type(line)), end='')
        print(']')


# 克拉默法则求解线性方程组
# A = 系数矩阵
def crame(A, b):
    A = np.array(A)
    b = np.array(b)

    # 检查是否为方阵，矩阵形状是否对应
    assert A.shape[0] == A.shape[1]
    assert A.shape[0] == b.shape[0]
    # 计算A的行列式
    A_d = np.linalg.det(A)
    if A_d == 0:
        print("该方程组系数矩阵行列式为0，无法求解！")
        return

    result = []
    # 计算方程组的解，系数矩阵有多少列就有多少解
    col_len = A.shape[1]
    for i in range(col_len):
        AA = numpy.copy(A)
        # 分别将值矩阵对第i列进行替换
        AA[::, i] = b
        det = np.linalg.det(AA)
        result.append(det / A_d)
    return result


# 返回拟合的方程结果
# precision = 精度，默认为4
def get_fit_fun_str(result, phi_str, precision: int = 4):
    assert len(result) == len(phi_str)
    expr = ''
    res_len = len(result)
    for i in range(res_len):
        num = ("{0:." + str(precision) + "f}").format(result[i])

        if i != 0 and num[0] != '-':
            expr += '+'
        expr += (num + phi_str[i])
    return expr


# 返回方程的字符串
def get_fun(result, phi_str):
    assert len(result) == len(phi_str)
    expr = ''
    res_len = len(result)
    for i in range(res_len):
        if i != 0:
            expr += '+'
        expr += ("{0}".format(result[i]) + phi_str[i])
    return expr


# 生成一个二次函数，即拟合函数
def get_fit(result, phi, x):
    assert len(result) == len(phi)
    sum = 0
    res_len = len(result)
    for i in range(res_len):
        sum += (phi[i](x)) * result[i]
    return sum


# 生成一个对数函数，即拟合函数
def get_ln_fit(t, a, b):
    temp = math.exp(b / t)
    return a * temp


# 计算误差
def get_diff(y, fx):
    assert len(y) == len(fx)
    sum = 0
    for i in range(len(y)):
        sum += (y[i] - fx[i]) ** 2
    return sum


if __name__ == '__main__':
    # 题文给出的
    t_str = '0	5	10	15	20	25 30	35	40	45	50	55'
    P_str = '0	1.27	2.16	2.86	3.44	3.87 4.15	4.37	4.51	4.58	4.62	4.64'

    # 获取温度t和占比P两个列表
    t, P = get_data(t_str, P_str)

    # 样本数：m=总数-1
    m = len(t) - 1

    print("-" * 5 + '使用二次函数拟合：')
    # 函数空间:phi=[1,x,x^2]
    phi = [lambda x: 1, lambda x: x, lambda x: x * x]
    # phi_str方便最后展示方程
    phi_str = ['', 'x', 'x^2']
    xishu = ['a' + str(elem) for elem in range(len(phi))]
    fun_str = get_fun(xishu, phi_str=phi_str)

    # 打印提示消息
    print("已知样本数有{0}个，令m={1}，拟合函数为 s(x)={2}".format(m + 1, m, fun_str))

    # 获得phi的计算值，每个下标是函数空间对应的
    phi_values = get_phi_value(t, phi)

    # 计算法方程中的G
    G = list(get_G(phi_values))
    print_list(G, name='G')

    # 计算法方程中的d
    d = list(get_d(phi_values, P))
    print_list(d, name='d')

    # 通过克拉默法则求解答案
    print("计算法方程 Ga=d，从而解得")
    result = crame(G, d)
    print('，'.join([str('a{}={}'.format(index, float(result[index]))) for index in range(len(result))]))
    # 修改precision可调精度,默认保留4位小数
    precision = 5
    fit_fun = get_fit_fun_str(result, phi_str, precision=precision)
    print("最终拟合出的方程为 s(x)={0} (保留{1}位)".format(fit_fun, precision))
    # 计算最后的拟合值的序列
    fx = [get_fit(result, phi, x) for x in t]
    diff = get_diff(fx=fx, y=P)
    print("误差为{0}".format(diff))

    print("\n" + "-" * 5 + '使用对数拟合：')
    # 将原来的P和t进行对数转换
    # 由于(0,0)在ln上不合法，暂时先去掉
    del P[0]
    del t[0]
    ln_P = [math.log(p) for p in P]
    ln_t = [(1 / tt) for tt in t]
    phi_ln = [lambda x: 1, lambda x: x]
    # phi_str_ln方便最后展示方程
    phi_str_ln = ['', 'x']
    phi_ln_values = get_phi_value(ln_t, phi_ln)
    G_ln = list(get_G(phi_ln_values))

    d_ln = list(get_d(phi_ln_values, ln_P))
    result_ln = crame(G_ln, d_ln)
    a_ln = math.exp(result_ln[0])
    b_ln = result_ln[1]

    fx_ln = [(a_ln * math.exp(b_ln / tt)) for tt in t]
    t.insert(0, 0)
    P.insert(0, 0)
    fx_ln.insert(0, 0)
    ln_diff = get_diff(fx=fx_ln, y=P)
    fit_ln_fun = ("{0:." + str(precision) + "f}*e^({1:." + str(precision) + "f}/t)").format(a_ln, b_ln)
    print("最终拟合出的方程为 s(x)={0} (保留{1}位)".format(fit_ln_fun, precision))
    print("误差为{0}".format(ln_diff))

    # 图表设置
    initial_plt(t, P, f=fx, fx_ln=fx_ln, is_show=True, fx_label='二次函数', ln_fx_label='对数函数')
