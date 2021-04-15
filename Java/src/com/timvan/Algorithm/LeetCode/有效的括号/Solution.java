package com.timvan.Algorithm.LeetCode.有效的括号;

import java.util.ArrayList;
import java.util.HashMap;

/**
 * <h3>蓝桥杯</h3>
 * <p></p>
 *
 * @author : TimVan
 * @date : 2021-04-15 15:56
 **/
public class Solution {
//    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
//    有效字符串需满足：
//    左括号必须用相同类型的右括号闭合。
//    左括号必须以正确的顺序闭合。
//
//    示例 1：
//    输入：s = "()"
//    输出：true
//    示例 2：
//
//    输入：s = "()[]{}"
//    输出：true
//    示例 3：
//
//    输入：s = "(]"
//    输出：false
//    示例 4：
//
//    输入：s = "([)]"
//    输出：false
//    示例 5：
//
//    输入：s = "{[]}"
//    输出：true
//    提示：
//            1 <= s.length <= 104
//    s 仅由括号 '()[]{}' 组成

    public boolean isValid(String s) {
        //保证s的长度大于等于1且不为奇数
        if (s.length() % 2 > 0) {
            return false;
        }
        ArrayList<Character> symbolList = new ArrayList<>();
        symbolList.add(s.charAt(0));
        //直接从第一个开始
        HashMap<Character, Character> bracketMap = new HashMap<>();
        bracketMap.put(')', '(');
        bracketMap.put(']', '[');
        bracketMap.put('}', '{');
        for (int i = 1; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            //如果是右括号，且不为空
            if (bracketMap.containsKey(currentChar) && !symbolList.isEmpty()) {
                char lastChar = symbolList.get(symbolList.size() - 1);
                if (lastChar == bracketMap.get(currentChar)) {
                    symbolList.remove(symbolList.size() - 1);
                } else {
                    return false;
                }
            } else {
                symbolList.add(currentChar);
            }
        }
        return symbolList.isEmpty();
    }

    public static void main(String[] args) {
        String str = "()[]{}";
        System.out.println(new com.timvan.Algorithm.LeetCode.有效的括号
                .Solution().isValid(str));
        str = "()";
        System.out.println(new com.timvan.Algorithm.LeetCode.有效的括号
                .Solution().isValid(str));
        str = "(]";
        System.out.println(new com.timvan.Algorithm.LeetCode.有效的括号
                .Solution().isValid(str));
        str = "([)]";
        System.out.println(new com.timvan.Algorithm.LeetCode.有效的括号
                .Solution().isValid(str));
    }
}
