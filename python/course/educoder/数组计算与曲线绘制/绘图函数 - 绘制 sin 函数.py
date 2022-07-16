# 请绘制sin函数曲线

import matplotlib
# matplotlib.use("Agg") # 设置平台绘图环境，勿删

import matplotlib.pyplot as plt

# 请在此添加代码实现函数细节   #
# ********** Begin *********#
# 已知坐标数据：

x = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360]
y = [0, 0.5, 0.866, 1, 0.866, 0.5, 0, -0.5, -0.866, -1, -0.866, -0.5, 0]
# 请你绘制sin函数曲线，图的marker 类型采用点状标记。

# 提示：只需绘制图像，并将图像保存为文件，不用展示图像(show())，程序会进行验证。
plt.plot(x, y, marker='.', linestyle='')
plt.show()

# ********** End **********#

# plt.savefig('picture/step0/fig0.png')  # 存储输出图像，勿删
