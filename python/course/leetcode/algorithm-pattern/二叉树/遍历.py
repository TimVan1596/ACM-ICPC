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

    def dfsTraversal(self, root: TreeNode) -> List[int]:
        orderList = []
        stack = []
        point = root
        while point is not None or len(stack) > 0:
            orderList.append(point.val)
            if point.right is not None:
                stack.append(point.right)
            if point.left is not None:
                point = point.left
            elif len(stack) > 0:
                point = stack.pop()
            else:
                break
        return orderList

    def dfsDivide(self, root: TreeNode) -> List[int]:
        orderList = []
        if root is None:
            return []
        else:
            # 分治法：先放入中间，再放入递归左的结果，最后放入递归右
            orderList.append(root.val)
            leftOrderList = self.dfsDivide(root.left)
            if len(leftOrderList) > 0:
                orderList.extend(leftOrderList)
            rightOrderList = self.dfsDivide(root.right)
            if len(rightOrderList) > 0:
                orderList.extend(rightOrderList)
        return orderList

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        orderList = []
        if root is None:
            return []
        # 当前层的队列
        currentQueue = [root]
        # 下一层的队列
        nextQueue = []
        # 当前层的序列
        currentOrderList = []
        # 原理：逐个遍历当前层的节点，将其子节点存下，若为空则替换
        # 注意：1.每一层都需要一个list
        # 2.这里while的len(currentOrderList)非空是由于下一层若为空，上一层还有数据未进入
        while len(currentQueue) > 0 or len(currentOrderList) > 0:
            if len(currentQueue) > 0:
                point = currentQueue.pop(0)
                currentOrderList.append(point.val)
                if point.left is not None:
                    nextQueue.append(point.left)
                if point.right is not None:
                    nextQueue.append(point.right)
            else:
                orderList.append(currentOrderList)
                currentOrderList = []
                currentQueue.extend(nextQueue)
                nextQueue = []
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
    # DFS
    print(solution.dfsTraversal(myBinaryTree))
    # DFS
    print(solution.dfsDivide(myBinaryTree))
    # BFS
    print(solution.levelOrder(myBinaryTree))

    #           A
    #    B             C
    # D     E      F      G
    # 深度优先遍历
    # A B D E C F G
