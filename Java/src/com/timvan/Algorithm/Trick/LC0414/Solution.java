package com.timvan.Algorithm.Trick.LC0414;

/**
 * <h3>蓝桥杯</h3>
 * <p></p>
 *
 * @author : TimVan
 * @date : 2021-04-14 16:31
 **/
class Solution {

//    给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
//
//    回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
//
//            ?
//
//    示例 1：
//
//    输入：x = 121
//    输出：true
//    示例?2：
//
//    输入：x = -121
//    输出：false
//    解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
//    示例 3：
//
//    输入：x = 10
//    输出：false
//    解释：从右向左读, 为 01 。因此它不是一个回文数。
//    示例 4：
//
//    输入：x = -101
//    输出：false
//
//    提示：
//
//    进阶：你能不将整数转为字符串来解决这个问题吗？


    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        int y = x;
        int reverse = 0;
        while (y > 0) {
            reverse = reverse * 10 + (int) (y % 10);
            y /= 10;
        }
        return reverse == x;
    }

    public static void main(String[] args) {
        int x = -121;
        System.out.println(new com.timvan.Algorithm.Trick.LC0414.Solution()
                .isPalindrome(x));
    }
}