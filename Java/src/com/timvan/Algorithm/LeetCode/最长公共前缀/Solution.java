package com.timvan.Algorithm.LeetCode.�����ǰ׺;

import java.time.chrono.MinguoChronology;

/**
 * <h3>���ű�</h3>
 * <p></p>
 *
 * @author : TimVan
 * @date : 2021-04-15 15:28
 **/
class Solution {
//    ��дһ�������������ַ��������е������ǰ׺��
//    ��������ڹ���ǰ׺�����ؿ��ַ���""��
//
//    ʾ�� 1��
//
//    ���룺strs =["flower","flow","flight"]
//    �����"fl"
//    ʾ�� 2��
//
//    ���룺strs =["dog","racecar","car"]
//    �����""
//    ���ͣ����벻���ڹ���ǰ׺��
//    ��ʾ��
//            0<=strs.length <=200
//            0<=strs[i].length <=200
//    strs[i]����СдӢ����ĸ���

    public String longestCommonPrefix(String[] strs) {
        int minLength = 201;
        //�����������һ��ֱ�ӷ���
        if (strs.length == 0) {
            return "";
        } else if (strs.length == 1) {
            return strs[0];
        }
        for (String str : strs) {
            //����ַ���ֱ�ӷ���
            if (str.length() == 0) {
                return "";
            } else if (str.length() < minLength) {
                minLength = str.length();
            }
        }
        //��������ж��
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
        System.out.println(new com.timvan.Algorithm.LeetCode.�����ǰ׺
                .Solution().longestCommonPrefix(roman));
        String[] roman1 = {"dog", "racecar", "car"};
        System.out.println(new com.timvan.Algorithm.LeetCode.�����ǰ׺
                .Solution().longestCommonPrefix(roman1));
        String[] roman2 = {"cir", "car"};
        System.out.println(new com.timvan.Algorithm.LeetCode.�����ǰ׺
                .Solution().longestCommonPrefix(roman2));
    }
}
