# -*- coding:utf-8 -*-
# @Time:2020/6/16 11:40
# @Author:TimVan
# @File:2. Add Two Numbers.py
# @Software:PyCharm

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        listNode3 = ListNode(0)
        p3 = listNode3
        # 每次相加的进位
        rest = 0
        while p1 is not None:
            val1 = p1.val
            val2 = p2.val

            p3.val = (rest + val1 + val2) % 10
            rest = int((rest + val1 + val2) / 10)
            p1 = p1.next
            if p1 is not None:
                p2 = p2.next
                p3.next = ListNode(0)
                p3 = p3.next
        return listNode3


myL1 = ListNode(2)
myL1.next = ListNode(4)
myL1.next.next = ListNode(3)

myL2 = ListNode(5)
myL2.next = ListNode(6)
myL2.next.next = ListNode(4)

solution = Solution()
listNode = solution.addTwoNumbers(myL1, myL2)
while listNode is not None:
    print(listNode.val)
    listNode = listNode.next
