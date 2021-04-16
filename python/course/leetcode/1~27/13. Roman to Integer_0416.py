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

class Solution:

    def romanToInt(self, s: str) -> int:
        s = s.replace('IV', 'a')
        s = s.replace('IX', 'b')
        s = s.replace('XL', 'c')
        s = s.replace('XC', 'd')
        s = s.replace('CD', 'e')
        s = s.replace('CM', 'f')
        result = 0
        for ch in range(len(s)):
            currentChar = s[ch]
            # print(currentChar)
            result += self.getValue(currentChar)
        return result

    def getValue(self, ch: str) -> int:
        if ch == 'I':
            return 1
        elif ch == 'V':
            return 5
        elif ch == 'X':
            return 10
        elif ch == 'L':
            return 50
        elif ch == 'C':
            return 100
        elif ch == 'D':
            return 500
        elif ch == 'M':
            return 1000
        elif ch == 'a':
            return 4
        elif ch == 'b':
            return 9
        elif ch == 'c':
            return 40
        elif ch == 'd':
            return 90
        elif ch == 'e':
            return 400
        elif ch == 'f':
            return 900


solution = Solution()
myStr = ['III', 'IV', 'IX', 'LVIII', 'MCMXCIV', 'DCXXI']
for single in myStr:
    print(solution.romanToInt(single))
