package com.timvan.Algorithm.LeetCode.��Ч������;

import java.util.ArrayList;
import java.util.HashMap;

/**
 * <h3>���ű�</h3>
 * <p></p>
 *
 * @author : TimVan
 * @date : 2021-04-15 15:56
 **/
public class Solution {
//    ����һ��ֻ���� '('��')'��'{'��'}'��'['��']' ���ַ��� s ���ж��ַ����Ƿ���Ч��
//    ��Ч�ַ��������㣺
//    �����ű�������ͬ���͵������űպϡ�
//    �����ű�������ȷ��˳��պϡ�
//
//    ʾ�� 1��
//    ���룺s = "()"
//    �����true
//    ʾ�� 2��
//
//    ���룺s = "()[]{}"
//    �����true
//    ʾ�� 3��
//
//    ���룺s = "(]"
//    �����false
//    ʾ�� 4��
//
//    ���룺s = "([)]"
//    �����false
//    ʾ�� 5��
//
//    ���룺s = "{[]}"
//    �����true
//    ��ʾ��
//            1 <= s.length <= 104
//    s �������� '()[]{}' ���

    public boolean isValid(String s) {
        //��֤s�ĳ��ȴ��ڵ���1�Ҳ�Ϊ����
        if (s.length() % 2 > 0) {
            return false;
        }
        ArrayList<Character> symbolList = new ArrayList<>();
        symbolList.add(s.charAt(0));
        //ֱ�Ӵӵ�һ����ʼ
        HashMap<Character, Character> bracketMap = new HashMap<>();
        bracketMap.put(')', '(');
        bracketMap.put(']', '[');
        bracketMap.put('}', '{');
        for (int i = 1; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            //����������ţ��Ҳ�Ϊ��
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
        System.out.println(new com.timvan.Algorithm.LeetCode.��Ч������
                .Solution().isValid(str));
        str = "()";
        System.out.println(new com.timvan.Algorithm.LeetCode.��Ч������
                .Solution().isValid(str));
        str = "(]";
        System.out.println(new com.timvan.Algorithm.LeetCode.��Ч������
                .Solution().isValid(str));
        str = "([)]";
        System.out.println(new com.timvan.Algorithm.LeetCode.��Ч������
                .Solution().isValid(str));
    }
}
