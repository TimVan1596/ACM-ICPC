# -*- coding:utf-8 -*-
# @Time:2021/5/10 13:59
# @Author:TimVan
# @File:Solution.py
# @Software:PyCharm
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        orderList = []
        # 定义一个栈，先进后出
        stack = []
        point = root
        while point is not None:
            # 打印当前节点
            orderList.append(point.val)
            # 右节点是否为空，非空放入栈
            if point.right is not None:
                stack.append(point.right)
            # 左节点如非空则进入，若为空从栈中取顶值
            if point.left is not None:
                point = point.left
            elif len(stack) > 0:
                point = stack.pop()
            else:
                break
        return orderList

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        orderList = []
        stack = []
        point = root
        while point is not None or len(stack) > 0:
            # 当前节点存在，继续找左节点
            if point is not None:
                stack.append(point)
                point = point.left
            # 当前节点若不存在，说明上一个进栈的为中结点，打印后继续找右节点
            else:
                point = stack.pop()
                # print(point.val)
                orderList.append(point.val)
                point = point.right
        return orderList

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        orderList = []
        stack = []
        point = root
        while point is not None or len(stack) > 0:
            if point is not None:
                stack.append(point)
                point = point.left
            else:
                point = stack.pop()

        return orderList


if __name__ == '__main__':
    myBinaryTree = TreeNode('A')
    BNode = TreeNode('B')
    CNode = TreeNode('C')
    DNode = TreeNode('D')
    ENode = TreeNode('E')
    FNode = TreeNode('F')
    GNode = TreeNode('G')
    myBinaryTree.left = BNode
    myBinaryTree.left.left = DNode
    myBinaryTree.left.right = ENode
    myBinaryTree.right = CNode
    myBinaryTree.right.left = FNode
    myBinaryTree.right.right = GNode
    solution = Solution()
    # 先序遍历
    print(solution.preorderTraversal(myBinaryTree))
    # 中序遍历
    print(solution.inorderTraversal(myBinaryTree))
