package com.timvan.Algorithm.LeetCode.最长公共前缀;

import java.time.chrono.MinguoChronology;

/**
 * <h3>蓝桥杯</h3>
 * <p></p>
 *
 * @author : TimVan
 * @date : 2021-04-15 15:28
 **/
class Solution {
//    编写一个函数来查找字符串数组中的最长公共前缀。
//    如果不存在公共前缀，返回空字符串""。
//
//    示例 1：
//
//    输入：strs =["flower","flow","flight"]
//    输出："fl"
//    示例 2：
//
//    输入：strs =["dog","racecar","car"]
//    输出：""
//    解释：输入不存在公共前缀。
//    提示：
//            0<=strs.length <=200
//            0<=strs[i].length <=200
//    strs[i]仅由小写英文字母组成

    public String longestCommonPrefix(String[] strs) {
        int minLength = 201;
        //如空数组或仅含一组直接返回
        if (strs.length == 0) {
            return "";
        } else if (strs.length == 1) {
            return strs[0];
        }
        for (String str : strs) {
            //如空字符串直接返回
            if (str.length() == 0) {
                return "";
            } else if (str.length() < minLength) {
                minLength = str.length();
            }
        }
        //逐个增加判断最长
        StringBuilder commonPrefix = new StringBuilder();
        for (int i = 0; i < minLength; i++) {
            char current = strs[0].charAt(i);
            int j = 1;
            for (j = 1; j < strs.length; j++) {
                if (strs[j].charAt(i) != current) {
                    return commonPrefix.toString();
                }
            }
            if (j == strs.length) {
                commonPrefix.append(current);
            }
        }
        return commonPrefix.toString();
    }

    public static void main(String[] args) {
        String[] roman = {"flower", "flow", "flight"};
        System.out.println(new com.timvan.Algorithm.LeetCode.最长公共前缀
                .Solution().longestCommonPrefix(roman));
        String[] roman1 = {"dog", "racecar", "car"};
        System.out.println(new com.timvan.Algorithm.LeetCode.最长公共前缀
                .Solution().longestCommonPrefix(roman1));
        String[] roman2 = {"cir", "car"};
        System.out.println(new com.timvan.Algorithm.LeetCode.最长公共前缀
                .Solution().longestCommonPrefix(roman2));
    }
}
