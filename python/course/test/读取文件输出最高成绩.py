# -*- coding:utf-8 -*-
# @Time:2020/8/3 4:25
# @Author:TimVan
# @File:读取文件输出最高成绩.py
# @Software:PyCharm

# 假设有一个学生成绩信息的数据文件，文件内容每行有姓名、学号、总学
# 分、总绩点数。这四个值有制表符分隔。如：gpa.txt内容如下：
# 赵一      3100001     160     608
# 李二      3100002     165     610
# 张三      3100003     160     600
# 王四      3100004     158     585
# 孙五      3100005     155     480
# 吴六      3100006     170     605
# 编写一个程序，首先读取gpa.txt文件内容，然后计算GPA最高的学生，最
# 后打印这个学生的名字、学号、总学分和GPA.

# 1、编写学生类，初始化计算GPA方法，打印信息；静态类读取
# 2、GPA = 绩点除学分
# 3、遍历查找打印最高值GPA学生的信息

class Student:
    name = ''
    no = ''
    # 总学分
    credit = 0
    # 总绩点数
    point = 0
    GPA = 0.0

    def __init__(self, name, no, credit, point):
        self.point = point
        self.no = no
        self.credit = credit
        self.name = name
        self.GPA = round(point / credit, 2)

    # 打印信息
    def printInfo(self):
        print("{0}\t{1}\t{2}\t{3}".format(self.name
                                          , self.no, self.credit, self.GPA))


# 读取文件输出最高成绩
def printMaxGpaFromFile():
    file = None
    try:
        # 读取文件
        file = open('gpa.txt', 'r')
    except FileNotFoundError as ret:
        print("文件异常：{0}".format(ret))
        return

    # 读取文件
    stuArr = []
    for line in file:
        # print(line, end='')
        stuInfo = line.strip().split()
        stu = Student(stuInfo[0], stuInfo[1], int(stuInfo[2]), int(stuInfo[3]))
        stuArr.append(stu)

    # 遍历查找打印最高值GPA学生的信息
    index = -1
    maxGpa = -1
    i = 0
    stuArrLen = len(stuArr)
    for i in range(stuArrLen):
        if stuArr[i].GPA > maxGpa:
            index = i
            maxGpa = stuArr[i].GPA

    if index < 0:
        print("学生信息有误")
    else:
        print("GPA最高的学生的信息为")
        stuArr[index].printInfo()


printMaxGpaFromFile()
