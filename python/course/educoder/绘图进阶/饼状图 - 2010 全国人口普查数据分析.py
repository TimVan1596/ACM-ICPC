# 请绘制育龄妇女的受教育程度分布饼图

import matplotlib
# matplotlib.use("Agg")

# 请编写代码绘制育龄妇女的受教育程度分布饼图，具体编程要求如下：
# 突出教育程度为初中的楔形，偏移占比设为 0.1 ；
# 饼图为等长等宽且有阴影；
# 楔形标签列表为['none', 'primary', 'junior', 'senior', 'specialties', 'bachelor', 'master']；
# 楔形的颜色分别为['red','orange','yellow','green','purple','blue','black']；
# 请存储输出图像，图像名字为 picture/step3/fig3.png 。
#  请在此添加实现代码  #
# ********** Begin *********#
#
import matplotlib.pyplot as plt
import numpy as np

labels = ['none', 'primary', 'junior', 'senior', 'specialties', 'bachelor', 'master']  # 标签
womenCount = [2052380, 11315444, 20435242, 7456627, 3014264, 1972395, 185028]
birthMen = [2795259, 12698141, 13982478, 2887164, 903910, 432333, 35915]
birthWomen = [2417485, 11000637, 11897674, 2493829, 786862, 385718, 32270]
liveMen = [2717613, 12477914, 13847346, 2863706, 897607, 429809, 35704]
liveWomen = [2362007, 10854232, 11815939, 2480362, 783225, 384158, 32136]
colors = ['red', 'orange', 'yellow', 'green', 'purple', 'blue', 'black']
explode = [0, 0, 0.1, 0, 0, 0, 0]
n = len(labels)

women_sum = sum(womenCount)
pers = list(map(lambda x: x / women_sum, womenCount))
plt.pie(pers, explode=explode, labels=labels, shadow=True, colors=colors,radius=1.1)
plt.axis('equal')   #该行代码使饼图长宽相等
# plt.savefig("picture/step3/fig3.png")
plt.show()

# ********** End **********#
