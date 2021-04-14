# -*- coding:utf-8 -*-
# @Time:2020/6/18 11:59
# @Author:TimVan
# @File:7. Reverse Integer.py
# @Software:PyCharm

# 给你一个
# 32
# 位的有符号整数
# x ，返回将
# x
# 中的数字部分反转后的结果。
#
# 如果反转后整数超过
# 32
# 位的有符号整数的范围[−231, 231 − 1] ，就返回
# 0。
#
# 假设环境不允许存储
# 64
# 位整数（有符号或无符号）。
#
#
# 示例
# 1：
#
# 输入：x = 123
# 输出：321
# 示例
# 2：
#
# 输入：x = -123
# 输出：-321
# 示例
# 3：
#
# 输入：x = 120
# 输出：21
# 示例
# 4：
#
# 输入：x = 0
# 输出：0
#
# 提示：
#
# -231 <= x <= 231 - 1


class Solution:
    def reverse(self, x: int) -> int:
        n = 0
        leadingZero = True
        isMinus = False
        if x < 0:
            isMinus = True
            x = -x
        while x > 0:
            rest = x % 10
            if leadingZero and (rest != 0):
                leadingZero = False
            if not leadingZero:
                n *= 10
                n += rest
            x //= 10
        if isMinus:
            n = -n
        # 越界检测
        if n < (-2 ** 31) or n > (2 ** 31 + 1):
            n = 0
        return n


myX: int = 123
myX = -10200
myX = 4294967296
solution = Solution()
print(solution.reverse(myX))
