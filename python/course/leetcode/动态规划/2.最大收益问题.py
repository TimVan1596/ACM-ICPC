# -*- coding:utf-8 -*-
# @Time:2020/7/4 20:55
# @Author:TimVan
# @File:2.最大收益问题.py
# @Software:PyCharm

# 最大收益问题
# 给一些任务，计算在一定时间内的最大收益的问题
# 任务的格式为（start，end，value）

def getMaxProfit(tasks: list) -> int:
    tasksLen = len(tasks)
    # 设置两个数组 opt[] = optimize[] 最优情况
    # 和 prev[] = previous[] 前一个可能任务序号
    # 坐标为0处代表不存在的值
    opt = [0] * (tasksLen + 1)
    prev = [0] * (tasksLen + 1)

    # 初始化生成prev[] 和 opt[]
    for i in range(1, tasksLen + 1, 1):
        task = tasks[i - 1]
        prev[i] = 0
        for j in range(i, 0, -1):
            # 判断是否有重合
            if tasks[j - 1][1] <= task[0] or tasks[j - 1][0] >= task[1]:
                prev[i] = j
                break
        opt[i] = max(opt[i - 1], task[2] + opt[prev[i]])
        # print("prev[%d] = %d" % (i, prev[i]))
        # print(tasks[i - 1], "-------", "opt[%d] = %d" % (i, opt[i]))
    return opt[tasksLen]


# （start，end，value）
inputArr = [
    # [(1, 4, 5), (3, 5, 1), (0, 6, 8), (4, 7, 4)
    #     , (3, 8, 6), (5, 9, 3), (6, 10, 2), (8, 11, 4)],
    [(1, 4, 100), (2, 5, 50), (5, 10, 200), (4, 8, 400), (9, 10, 150)]
]
for one in inputArr:
    print("-> %d" % getMaxProfit(one))
