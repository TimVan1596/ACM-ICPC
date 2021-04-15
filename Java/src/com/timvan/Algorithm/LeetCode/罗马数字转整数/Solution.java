package com.timvan.Algorithm.LeetCode.罗马数字转整数;

import java.util.HashMap;

/**
 * <h3>蓝桥杯</h3>
 * <p></p>
 *
 * @author : TimVan
 * @date : 2021-04-15 14:30
 **/
class Solution {

    //    罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
//
//    字符          数值
//    I             1
//    V             5
//    X             10
//    L             50
//    C             100
//    D             500
//    M             1000
//    例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
//
//    通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
//
//    I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
//    X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
//    C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
//    给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

    public int romanToInt(String s) {
        HashMap<String, Integer> alphaBet = new HashMap<>();
        alphaBet.put("I", 1);
        alphaBet.put("IV", 4);
        alphaBet.put("IX", 9);
        alphaBet.put("V", 5);
        alphaBet.put("X", 10);
        alphaBet.put("XL", 40);
        alphaBet.put("XC", 90);
        alphaBet.put("L", 50);
        alphaBet.put("C", 100);
        alphaBet.put("CD", 400);
        alphaBet.put("CM", 900);
        alphaBet.put("D", 500);
        alphaBet.put("M", 1000);

        int result = 0;
        int sLen = s.length();
        for (int i = 0; i < sLen; i++) {
            String currentSymbol = s.charAt(i) + "";
            //判断是否是6种特殊情况之一
            if ((i + 1 < sLen) && alphaBet
                    .containsKey(currentSymbol + s.charAt(i + 1) + "")) {
                currentSymbol = currentSymbol + s.charAt(i + 1) + "";
                i++;
            }
            result += alphaBet.get(currentSymbol);

        }
        return result;
    }

    public static void main(String[] args) {
        String roman = "MCMXCIV";
        System.out.println(new Solution().romanToInt(roman));
        roman = "III";
        System.out.println(new Solution().romanToInt(roman));
        roman = "IV";
        System.out.println(new Solution().romanToInt(roman));
        roman = "IX";
        System.out.println(new Solution().romanToInt(roman));
        roman = "LVIII";
        System.out.println(new Solution().romanToInt(roman));
    }


}