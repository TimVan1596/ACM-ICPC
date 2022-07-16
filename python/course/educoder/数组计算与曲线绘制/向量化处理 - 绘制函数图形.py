# 请编写代码实现向量化帽函数并绘制函数曲线

import matplotlib
# matplotlib.use("Agg")

#   请在此添加实现代码   #
# ********** Begin *********#
import matplotlib.pyplot as plt
import numpy as np


def H(x):
    if x < 0:
        return 0
    if x < 1:
        return float(x)
    if x < 2:
        return float(2 - x)
    if x >= 2:
        return 0


h = np.vectorize(H)
x = np.linspace(-3, 5, 1000)
y = h(x)
# y = [H(xx) for xx in x]
print("x=", x)
print("y=", y)

plt.plot(x, y, color='blue')
plt.title('Plotting hat func in this plot')
plt.show()
# plt.savefig("picture/step4/fig4.png")
# ********** End **********#
