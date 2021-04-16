# -*- coding:utf-8 -*-
# @Time:2020/6/21 16:22
# @Author:TimVan
# @File:20. Valid Parentheses.py
# @Software:PyCharm


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        bracketList = []
        bracket = {"}": "{", "]": "[", ")": "("}
        for i in range(len(s)):
            # 是否在表中
            if bracket.get(s[i]) is not None:
                if len(bracketList) <= 0 or bracketList[-1] != bracket.get(s[i]):
                    return False
                else:
                    bracketList.pop()
            else:
                bracketList.extend(s[i])
        return len(bracketList) == 0


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
