package com.timvan.Algorithm.LeetCode.外观数列_35;

/**
 * <h3>蓝桥杯</h3>
 * <p></p>
 *
 * @author : TimVan
 * @date : 2021-04-27 13:51
 **/
class Solution {

//    给定一个正整数 n ，输出外观数列的第 n 项。
//            「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
//    你可以将其视作是由递归公式定义的数字字符串序列：
//
//    countAndSay(1) = "1"
//    countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
//    前五项如下：
//            1.     1
//            2.     11
//            3.     21
//            4.     1211
//            5.     111221
//    第一项是数字 1
//    描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
//    描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
//    描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
//    描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"
//    要 描述 一个数字字符串，首先要将字符串分割为 最小 数量的组，每个组都由连续的最多 相同字符 组成。然后对于每个组，先描述字符的数量，然后描述字符，形成一个描述组。要将描述转换为数字字符串，先将每组中的字符数量用数字替换，再将所有描述组连接起来。
//
//    例如，数字字符串 "3322251" 的描述如下图：
//
//    示例 1：
//
//    输入：n = 1
//    输出："1"
//    解释：这是一个基本样例。
//    1 <= n <= 30

    public String countAndSay(int n) {
        if (n != 1) {
            StringBuilder result = new StringBuilder();
            //得到上一个字符串
            String lastStr = countAndSay(n - 1);
            int lastStrLen = lastStr.length();
            //前一个字符和其出现的数量
            char previousChar = lastStr.charAt(0);
            int previousCount = 1;
            for (int i = 1; i < lastStrLen; i++) {
                char current = lastStr.charAt(i);
                if (previousChar == current) {
                    previousCount++;
                } else {
                    //输出拼接
                    result.append(previousCount);
                    result.append(previousChar);
                    previousCount = 1;
                    previousChar = current;
                }
            }
            //输出拼接
            result.append(previousCount);
            result.append(previousChar);
            return result.toString();
        }
        //嵌套出口
        return "1";
    }

    public static void main(String[] args) {
        int n = 1;
        System.out.println(new Solution().countAndSay(n));
        n = 2;
        System.out.println(new Solution().countAndSay(n));
        n = 3   ;
        System.out.println(new Solution().countAndSay(n));
        n = 4;
        System.out.println(new Solution().countAndSay(n));
        n = 5;
        System.out.println(new Solution().countAndSay(n));
    }
}