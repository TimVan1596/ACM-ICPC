# -*- coding:utf-8 -*-
# @Time:2020/6/19 12:08
# @Author:TimVan
# @File:13. Roman to Integer.py
# @Software:PyCharm

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together.
# Twelve is written as, XII, which is simply X + II.
# The number twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.
# Example 1:
# Input: "III"
# Output: 3
#
# Example 2:
# Input: "IV"
# Output: 4
#
# Example 3:
# Input: "IX"
# Output: 9
#
# Example 4:
# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
#
# Example 5:
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


# class Solution:
#     def romanToInt(self, s: str) -> int:
#         romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50
#             , 'C': 100, 'D': 500, 'M': 1000
#             , 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
#         ret = 0
#         i = 0
#         strLen = len(s)
#         while i < strLen:
#             ch = s[i]
#             if (ch == 'I' or ch == 'X' or ch == 'C') and i + 1 < len(s):
#                 nextCH = ch + s[i + 1]
#                 if nextCH == 'IV' or nextCH == 'IX' \
#                         or nextCH == 'XL' or nextCH == 'XC' \
#                         or nextCH == 'CD' or nextCH == 'CM':
#                     ch = nextCH
#                     i += 1
#             ret += romanDict.get(ch, 0)
#             i += 1
#         return ret

# 解法2
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300, 'D': 500,
             'CM': 800, 'M': 1000}
        return sum(d.get(s[max(i - 1, 0):i + 1], d[n]) for i, n in enumerate(s))

# 解析
# 1、构建一个字典记录所有罗马数字子串，注意长度为2的子串记录的值是（实际值 - 子串内左边罗马数字代表的数值）
#
# 2、这样一来，遍历整个 ss 的时候判断当前位置和前一个位置的两个字符组成的字符串是否在字典内，如果在就记录值，不在就说明当前位置不存在小数字在前面的情况，直接记录当前位置字符对应值
#
# 举个例子，遍历经过 IV 的时候先记录 I的对应值 1，再往前移动一步记录 IV 的值 3，加起来正好是 IV 的真实值 4。
# max 函数在这里是为了防止遍历第一个字符的时候出现 [-1:0][−1:0] 的情况


solution = Solution()
myStr = ['III', 'IV', 'IX', 'LVIII', 'MCMXCIV', 'DCXXI']
for single in myStr:
    print(solution.romanToInt(single))
