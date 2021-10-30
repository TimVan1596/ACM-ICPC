# -*- coding:utf-8 -*-
# @Time:2020/6/18 11:59
# @Author:TimVan
# @File:7. Reverse Integer.py
# @Software:PyCharm

# 给你一个 32位的有符号整数x ，返回将x
# 中的数字部分反转后的结果。
# 如果反转后整数超过 32 位的有符号整数的范围[−231, 231 − 1] ，就返回0。
#
# 假设环境不允许存储 64 位整数（有符号或无符号）。
# 示例
# 1：
# 输入：x = 123
# 输出：321
# 示例2：
#

class Solution:
    def reverse(self, x: int) -> int:
        # 将x去掉符号然后字符串倒序
        result = int(str(abs(x))[::-1])
        if result > 2 ** 31 - 1:
            return 0
        if x < 0:
            result *= -1
        return result


solution = Solution()
num = 123
print(solution.reverse(num))
num = -123
print(solution.reverse(num))
num = 1534236469
print(solution.reverse(num))
