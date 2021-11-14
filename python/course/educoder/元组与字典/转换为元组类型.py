# coding=utf-8

# 初始化menu1字典，输入两道菜的价格
menu1 = {}
menu1['fish']=int(input())
menu1['pork']=int(input())

# menu_total列表现在只包含menu1字典
menu_total = [menu1]

# 请在此添加代码，实现编程要求
########## Begin ##########

# menu_total列表中初始时只包含menu1字典，menu1字典中包含两道菜和两道菜的价格；
#
# 编程要求是向menu_total列表中添加另外一个菜单字典menu2，menu2菜单中的菜名和menu1菜单一样，菜的价格是menu1菜的价格的2倍；
#
# 输出新的menu_total列表。
menu2 = menu1.copy()
for key in menu2.keys():
    value = menu2[key]
    value = value*2
    menu2[key] = value
menu_total.append(menu2)
########## End ##########

# 输出menu_total列表
print(menu_total)





