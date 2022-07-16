# coding=utf-8

# 创建并初始化my_menu列表
my_menu = ['pizza',
           'chicken',
           'carrot',
           'apple',
           'banana']

# 请在此添加代码，对my_menu列表进行切片操作
########## Begin ##########
# 利用切片方法从my_menu列表中每3个元素取1个，组成子序列并打印输出；
#
# 利用切片方法获取my_menu列表的最后三个元素组成子序列并打印输出。
sub = my_menu[::3]
print(sub)
sub = my_menu[-3:]
print(sub)
########## End ##########
