# -*- coding:utf-8 -*-
# @Time:2020/6/15 11:38
# @Author:TimVan
# @File:leetcode.py
# @Software:PyCharm
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers() :

    listNode3 = ListNode(0)
    p3 = listNode3
    print('----', p3.val)
    # 每次相加的进位
    rest = 0
    i = 0
    while p3 is not None:
        i += 1
        p3.val = i
        p3.next = ListNode(0)
        p3 = p3.next
        if i == 3:
            break
    return listNode3


listNode = addTwoNumbers()
while listNode is not None:
    print(listNode.val)
    listNode = listNode.next
