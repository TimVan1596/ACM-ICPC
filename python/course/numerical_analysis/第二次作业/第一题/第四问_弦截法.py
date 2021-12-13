def f(x):
    return x ** 3 - 3 * x - 1


if __name__ == '__main__':
    # x0 = 2，X1 = 1.2
    xs = [2, 1.2]
    for i in range(2, 6):
        f_x_k = f(xs[i - 1])
        f_x_km = f(xs[i - 2])
        # 弦截法迭代公式
        value = xs[i - 1] - ((xs[i - 1] - xs[i - 2]) * f_x_k / (f_x_k - f_x_km))
        xs.append(value)
        print("i={},f(x)={}".format(i, value))
