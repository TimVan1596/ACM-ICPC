# -*- coding:utf-8 -*-
# @Time:2020/6/13 18:54
# @Author:TimVan
# @File:异常练习.py
# @Software:PyCharm

# 1. 应用文件操作的相关知识，通过Python新建一个文件gushi.txt，选择一首古诗写入文件中
# 2. 另外写一个函数，读取指定文件gushi.txt，将内容复制到copy.txt中，并在控制台输出“复制完
# 毕”。
# 3. 提示：分别定义两个函数，完成读文件和写文件的操作
# 尽可能完善代码，添加异常处理。

# 写文件
# contentList = writeLines的内容
def writeFile(fileName, contentList):
    # 增加换行
    file = open(fileName, 'w')

    # file.writelines(line+'\n' for line in contentList)
    file.writelines(line for line in contentList)
    file.close()


# 读文件
# contentList = readLines的内容
def readFile(fileName):
    contentList = []
    try:
        file = open(fileName, 'r')
        try:
            contentList = file.readlines()
        except Exception as reason:
            print("[WRONG]文件打开异常,%s" % reason)
        finally:
            file.close()
    except Exception as reason:
        print("[WRONG]文件未打开,%s" % reason)
    return contentList


def main():
    gushiList = ['使至塞上', '唐 王维'
        , '单车欲问边，属国过居延。'
        , '征蓬出汉塞，归雁入胡天。'
        , '大漠孤烟直，长河落日圆。'
        , '萧关逢候骑，都护在燕然。']
    # 为每一行换行
    gushiList.append("\n")
    gushiList = (line + '\n' for line in gushiList)

    writeFile('gushi.txt', gushiList)
    contentList = readFile('gushi.txt')
    writeFile('copy.txt', contentList)
    print("复制完毕")


main()
