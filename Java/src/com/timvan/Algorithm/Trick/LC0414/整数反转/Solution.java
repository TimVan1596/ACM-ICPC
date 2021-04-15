package com.timvan.Algorithm.Trick.LC0414.整数反转;

import static java.lang.Math.pow;

/**
 * <h3>蓝桥杯</h3>
 * <p>7. 整数反转</p>
 *
 * @author : TimVan
 * @date : 2021-04-14 15:53
 **/
public class Solution {
//    给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
//    如果反转后整数超过 32 位的有符号整数的范围 [?231,  231 ? 1] ，就返回 0。

//    假设环境不允许存储 64 位整数（有符号或无符号）。
//    示例 1：
//    输入：x = 123
//    输出：321
//    示例 2：
//
//    输入：x = -123
//    输出：-321
//    示例 3：
//
//    输入：x = 120
//    输出：21
//    示例 4：
//
//    输入：x = 0
//    输出：0
//             
//    提示：
//            -231 <= x <= 231 - 1

    public int reverse(int x) {
        int y = x;
        if (x < 0) {
            y *= -1;
        }
        double MAX_SIZE = pow(2, 31) - 1;
        double bigResult = 0;
        while (y > 0) {
            bigResult =bigResult*10 + (int)(y % 10);
            y /= 10;
        }
        if (bigResult > MAX_SIZE) {
            return 0;
        }
        if (x < 0) {
            bigResult *= -1;
        }
        return (int) bigResult;
    }

    public static void main(String[] args) {
        int x = 120;
        System.out.println(new Solution().reverse(x));

    }
}
