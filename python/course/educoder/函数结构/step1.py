# coding=utf-8

# 输入两个正整数a,b
a = 16
b = 40


# 请在此添加代码，求两个正整数的最大公约数
########## Begin ##########

def gcd(a, b):
    s = a * b
    while a % b != 0:
        a, b = b, (a % b)

    return s//b


########## End ##########

# 调用函数，并输出最大公约数
print(gcd(a, b))
