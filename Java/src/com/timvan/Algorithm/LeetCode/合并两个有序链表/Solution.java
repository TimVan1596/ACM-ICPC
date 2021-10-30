package com.timvan.Algorithm.LeetCode.合并两个有序链表;

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

    //将两个升序链表合并为一个新的 升序 链表并返回。
    // 新链表是通过拼接给定的两个链表的所有节点组成的。
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode newList = new ListNode();
        ListNode l1Pointer = l1;
        ListNode l2Pointer = l2;
        ListNode newPointer = newList;
        if (l1Pointer == null && l2Pointer == null) {
            return null;
        }

        //逐个比较然后向下一个
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
        //若一方为空就全部覆盖
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