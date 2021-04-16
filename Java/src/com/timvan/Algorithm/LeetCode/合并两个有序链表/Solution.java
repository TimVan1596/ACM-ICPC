package com.timvan.Algorithm.LeetCode.�ϲ�������������;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */


class Solution {
    static class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    //��������������ϲ�Ϊһ���µ� ���� �������ء�
    // ��������ͨ��ƴ�Ӹ�����������������нڵ���ɵġ�
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode newList = new ListNode();
        ListNode l1Pointer = l1;
        ListNode l2Pointer = l2;
        ListNode newPointer = newList;
        if (l1Pointer == null && l2Pointer == null) {
            return null;
        }

        //����Ƚ�Ȼ������һ��
        while (l1Pointer != null && l2Pointer != null) {
            if (l1Pointer.val <= l2Pointer.val) {
                newPointer.val = l1Pointer.val;
                l1Pointer = l1Pointer.next;
            } else {
                newPointer.val = l2Pointer.val;
                l2Pointer = l2Pointer.next;
            }
            newPointer.next = new ListNode();
            newPointer = newPointer.next;
        }
        //��һ��Ϊ�վ�ȫ������
        if (l1Pointer != null) {
            newPointer.val = l1Pointer.val;
            newPointer.next = l1Pointer.next;
        } else if (l2Pointer != null) {
            newPointer.val = l2Pointer.val;
            newPointer.next = l2Pointer.next;
        }
        return newList;
    }

    public static void main(String[] args) {
//        ListNode l1 = new ListNode(1);
//        l1.next = new ListNode(3);
//        l1.next.next = new ListNode(5);
//        ListNode l2 = new ListNode(1);
//        l2.next = new ListNode(2);
//        l2.next.next = new ListNode(4);
//        ListNode newList = new Solution().mergeTwoLists(l1, l2);
//        while (newList != null) {
//            System.out.println(newList.val);
//            newList = newList.next;
//        }
        ListNode l1 = new ListNode();
        ListNode l2 = new ListNode();
        ListNode newList = new Solution().mergeTwoLists(l1, l2);
        while (newList != null) {
            System.out.println(newList.val);
            newList = newList.next;
        }
    }
}