# -*- coding: utf-8 -*-
import matplotlib

# matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

xstring = '2015 2014 2013 2012 2011	 \
           2010 2009 2008 2007 2006	 \
           2005 2004 2003 2002 2001	2000'  # x轴标签

n = 6
ystring = [''] * n  # y轴对应的6组数据
ystring[0] = '6793	6324	6237	5790.99	5357.1	5032	4681	3800	3863.9	3366.79	3167.66	2778	2359	2250	2170	2112'
ystring[1] = '6473	5933	5850	5429.93	4993.17	4725	4459	3576	3645.18	3119.25	2936.96	2608	2197	2092	2017	1948'
ystring[2] = '15157	12965	12591	11460.19	10993.92	10934	9662	7801	7471.25	6584.93	5833.95	5576	4145	4154	4348	4288'
ystring[3] = '12914	11826	12997	12306.41	12327.28	11406	10608	8378	8667.02	8052.78	6922.52	5744	4196	4336	4588	4751'
ystring[
    4] = '9566	9817	9777	9020.91	8488.21	7747	6871	5886	5773.83	5246.62	5021.75	3884	3675.14	3488.57	3273.53	3260.38'
ystring[
    5] = '4845	5177	4907	4305.73	4182.11	4099	3671	3219	3351.44	3131.31	2829.35	2235	2240.74	1918.83	2033.08	1864.37'

labels = ['Commercial housing', 'Residential commercial housing',
          'high-end apartments', 'Office Building', 'Business housing', 'Others']  # 图例标签
colors = ['#ff7f50', '#87cefa', '#DA70D6', '#32CD32', '#6495ED', '#FF69B4']  # 指定颜色

#  请在此添加实现代码  #
# ********** Begin *********#
# 请编写代码绘制六类商品房平均销售价格柱状图，具体编程要求如下：
# 柱状图柱形宽度设置为 0.8 ，颜色分别为列表colors中对应的 RGB 值；
# 横轴坐标轴范围为 [-1, 98] ，第一组数据的柱形起始位分别为 1,7,13,...91 ，间隔为 6 ；
# 横轴标签为年份，从 2000 至 2015 ，旋转角度为 45 度，标签位置位于 6 组数据正中间；
# 纵轴坐标轴范围为 [1450, 15300] ，轴刻度为 2000, 4000, ...14000 ，刻度间隔为 2000 ；
# 添加图例，图例标签如列表legend_labels所示，位置位于左上角；
# 添加标题'Selling Prices of Six Types of Housing'；
# 存储输出图像，图像名字为 picture/step2/fig2.png 。
import numpy as np

bar_width = 0.8


def proc(ori_str: str):
    data = ori_str.split()
    data.reverse()
    return data


y_list = list(map(proc, ystring))
x_list = proc(xstring)
x_index = np.arange(len(x_list))

data_len = len(x_list)

# x轴的列表
xticks = [i for i in range(-1, 98 + 1)]
# 初始化绘图参数
plt.yticks([elem for elem in range(2000, 14000 + 1, 2000)])
plt.ylim(1450, 15300)
plt.xlim(-1, 98)
plt.xticks([ii * 6 + 1 + bar_width * 2.5 for ii in range(0, data_len)], x_list, rotation=45)

for i in range(n):
    temp = [ii * 6 + 1 + i * bar_width for ii in range(0, data_len)]
    print("i=", i)
    print("temp=", temp)
    values = list(map(lambda x: float(x), y_list[i]))
    print("values=", values)
    plt.bar(temp, values, color=colors[i],
            width=bar_width,
            label=labels[i])
    print("-" * 10)

plt.legend()
plt.title('Selling Prices of Six Types of Housing')
plt.show()
# ********** End **********#
