# import matplotlib.pyplot as plt  # 导入 matplotlib 库
# from math import sin, radians  # 导入数学计算库
#
# x = range(0, 361)  # 创建 0-360 的整数列表
# y = [sin(radians(e)) for e in x]  # 获得 x 对应的正弦值，以列表存储
# plt.figure(figsize=[8, 5])  # 在绘图之前设置画布大小，宽为 8 英尺，高为 5 英尺
# plt.plot(x, y)  # 绘制曲线
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
#
# t = np.arange(0.0, 2.0, 0.01)
# s1 = np.sin(2 * np.pi * t)
# s2 = np.sin(4 * np.pi * t)
# plt.subplot(211)  # 绘图区域被分为 2 行 1 列，接下来绘制第一幅图
# plt.plot(t, s1)
# ax2 = plt.subplot(212)  # 绘制第二幅图
# plt.plot(t, 2 * s1)
# plt.show()


import matplotlib

# matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

labels = ['none', 'primary', 'junior', 'senior', 'specialties', 'bachelor', 'master']  # 标签
womenCount = [2052380, 11315444, 20435242, 7456627, 3014264, 1972395, 185028]
birthMen = [2795259, 12698141, 13982478, 2887164, 903910, 432333, 35915]
birthWomen = [2417485, 11000637, 11897674, 2493829, 786862, 385718, 32270]
liveMen = [2717613, 12477914, 13847346, 2863706, 897607, 429809, 35704]
liveWomen = [2362007, 10854232, 11815939, 2480362, 783225, 384158, 32136]

#  请在此添加实现代码  #
# ********** Begin *********#
# 编程要求
# 2010 年全国按受教育程度分的 15 - 64 岁妇女平均活产子女数和平均存活子女数如下表所示：
#
# 请编写代码绘制图像，详细数据在右侧代码中已给出，具体编程要求如下：
# 包括两幅子图，左图是不同受教育程度育龄妇女生育子女的平均个数统计（按存活子女数统计）
# 右图是不同受教育程度育龄妇女生育子女的存活比例（即存活子女数/活产子女数）；
# 画布大小的宽高分别为 14, 5 英尺；
# 两幅子图都需添加横轴标签，标签列表labels在右侧代码中已给出；
# 左图线条颜色设置为红色red，线性采用默认设置；
# 右图线条颜色设置为蓝色blue，线性采用默认设置；
# 请存储输出图像，图像名字为 picture/step4/fig4.png 。
# 完成图应如下图所示：
plt.figure(figsize=[14, 5])
n = len(labels)
x = np.arange(0, n)
birth = [birthMen[i] + birthWomen[i] for i in range(n)]
live = [liveMen[i] + liveWomen[i] for i in range(n)]
avg = [live[i] / womenCount[i] for i in range(n)]
per_live = [live[i] / birth[i] for i in range(n)]

plt.subplot(121)
plt.plot(x, avg, color='red')
plt.xticks(x, labels=labels)

plt.subplot(122)
plt.plot(x, per_live, color='blue')
plt.xticks(x, labels=labels)
plt.savefig("picture/step4/fig4.png")
plt.show()

# ********** End **********#
