# 请编写代码绘制住宅商品房平均销售价格柱状图

import matplotlib

# matplotlib.use("Agg")

#  请在此添加实现代码  #
# ********** Begin *********#


# 请编写代码绘制办公楼商品房平均销售价格柱状图，具体图像要求如下：
# 横轴标签为年份，从 2000 至 2015 ，旋转角度为 45 度；
# 纵轴标签为销售价格，坐标轴范围为 [4000, 13500] ，轴刻度为 4000，5000，6000，...13000 ，刻度间隔为 1000 ；
# 柱状图颜色为紫色，对应的RGB值为 #800080 ，柱形宽度为默认宽度;
# 存储输出图像，图像名字为 picture/step1/fig1.png 。
import matplotlib.pyplot as plt

years = '[2015 2014 2013 2012 2011 2010 2009 2008 2007 2006 2005 2004 2003 2002 2001 2000]'
prices = '[12914 11826 12997 12306.41 12327.28 11406 10608 8378 8667.02 8052.78 6922.52 5744 4196 4336 4588 4751]'
years = years[1:-1]
years = years.split()
years.reverse()

prices = prices[1:-1]
prices = prices.split()
prices = list(map(lambda x: float(x), prices))
prices.reverse()
print(prices)

y_labels = [elem for elem in range(4000, 13000 + 1, 1000)]
y_index = [index for index in range(0, 10)]

print(y_labels)
print(y_index)
plt.yticks(y_labels, y_labels)
plt.ylim(y_labels[0], 13500)

plt.bar(years, prices, color='#800080')
plt.xticks(rotation=45)
# plt.savefig('picture/step1/fig1.png')
plt.show()

# ********** End **********#
