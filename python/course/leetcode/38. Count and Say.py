# -*- coding:utf-8 -*-
# @Time:2020/6/27 10:26
# @Author:TimVan
# @File:38. Count and Say.py
# @Software:PyCharm

# # 38. Count and Say
# The count-and-say sequence is the sequence of integers with the first five terms as following:
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n where 1 ≤ n ≤ 30,
# generate the nth term of the count-and-say sequence.
# You can do so recursively,
# in other words from the previous member read off the digits,
# counting the number of digits in groups of the same digit.
#
# Note: Each term of the sequence of integers will be represented as a string.
# Example 1:
# Input: 1
# Output: "1"
# Explanation: This is the base case.

# Example 2:
# Input: 4
# Output: "1211"
# Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1"
# , "2" can be read as "12" which means frequency = 1 and value = 2
# , the same way "1" is read as "11"
# , so the answer is the concatenation of "12" and "11" which is "1211".


class Solution:
    def countAndSay(self, n: int) -> str:
        lastStr = "1"
        for i in range(1, n, 1):
            currentStr = ""
            ch = lastStr[0]
            num = 1
            for j in range(1, len(lastStr), 1):
                if lastStr[j] == ch:
                    num += 1
                else:
                    currentStr = currentStr+str(num)+ch
                    ch = lastStr[j]
                    num = 1
            # 结束后仍有剩余
            currentStr = currentStr + str(num) + ch
            lastStr = currentStr
        return lastStr


solution = Solution()
inputArr = [
    1
    ,
    2
    ,
    3
    , 4
    , 5
    , 6
    , 7]

for one in inputArr:
    print(solution.countAndSay(one))
