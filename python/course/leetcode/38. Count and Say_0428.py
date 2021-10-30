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

# "1"
# "11"
# "21"
# "1211"

class Solution:
    def countAndSay(self, n: int) -> str:
        current = "1"
        # 才下标1开始计算，0直接输出“1”
        for i in range(1, n):
            # cnt=记录重复个数，lastChar=检测重复的字符,temp=暂存的描述字符串
            cnt = 1
            lastChar = current[0]
            temp = ""
            for j in range(1, len(current)):
                if lastChar == current[j]:
                    cnt += 1
                else:
                    temp += str(cnt) + lastChar
                    cnt = 1
                    lastChar = current[j]
            temp += str(cnt) + lastChar
            current = temp
        return current


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
