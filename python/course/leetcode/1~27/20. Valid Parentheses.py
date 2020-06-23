# -*- coding:utf-8 -*-
# @Time:2020/6/21 16:22
# @Author:TimVan
# @File:20. Valid Parentheses.py
# @Software:PyCharm

# 20. Valid Parentheses.py
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
# Input: "()"
# Output: true
#
# Example 2:
# Input: "()[]{}"
# Output: true
#
# Example 3:
# Input: "(]"
# Output: false
#
# Example 4:
# Input: "([)]"
# Output: false
#
# Example 5:
# Input: "{[]}"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        # 奇数则直接退出
        if len(s) % 2 != 0:
            return False

        # 将元素填充进list，并把list看作一个栈
        bracketDict = {'(': ')', '[': ']', '{': '}'}
        bracketStack = []
        for single in s:
            if single in bracketDict.keys():
                bracketStack.append(single)
            elif single in bracketDict.values():
                # 栈空情况下只有close括号
                if len(bracketStack) == 0:
                    return False
                # 判断对应顺序
                if bracketDict.get(bracketStack[-1]) == single:
                    bracketStack.pop()
                    continue
                else:
                    return False
        if len(bracketStack) == 0:
            return True
        else:
            return False


solution = Solution()
inputStrArr = [
    "{[]}()[]{}"
    , ""
    , "})"
    , "{()}[])"
    , "([)]"
    , "{[]}()["
]
for one in inputStrArr:
    print(solution.isValid(one))
