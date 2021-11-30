import math


import numpy as np

# 梯度检验
# 第一步、首先需要给出原函数、导函数、自变量的求导点和精度epsilon
# 第二步、分别求出梯度值和求导值
# 第三步、求出diff并与epsilon对比，返回是否正常和diff
def grad_check(fun, d_fun, x, theta=1e-4, epsilon=1e-3):
    def grad():
        first = fun(x + theta)
        second = fun(x - theta)
        return (first - second) / (2 * theta)

    def l2(val):
        return (val ** 2) ** 0.5

    gradient = grad()
    derivation = d_fun(x)
    print("gradient=", gradient)
    print("derivation=", derivation)

    diff = l2(gradient - derivation) / (l2(gradient) + l2(derivation))
    return diff < epsilon, diff


if __name__ == '__main__':
    # fun为原函数，d_fun为导函数
    def fun(x):
        return x * x


    def d_fun(x):
        return 2 * x


    my_epsilon = 1e-5
    my_theta = 1e-5
    my_x = 4
    is_good, diff = grad_check(fun=fun, d_fun=d_fun, x=my_x, theta=my_theta, epsilon=my_epsilon)
    print("is_good=", is_good)
    print("diff=", diff)

    print("-" * 15)
    my_x = np.linspace(1, 6, 6, dtype=int).reshape(2, 3)
    print("my_x=", my_x)
    vfun = np.vectorize(fun)
    print("vfun(my_x)=", vfun(my_x))

    is_good, diff = grad_check(fun=fun, d_fun=d_fun, x=my_x, theta=my_theta, epsilon=my_epsilon)
    print("is_good=", is_good)
    print("diff=", diff)
