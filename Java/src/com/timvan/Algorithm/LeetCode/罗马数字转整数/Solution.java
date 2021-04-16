package com.timvan.Algorithm.LeetCode.��������ת����;

import java.util.HashMap;

/**
 * <h3>���ű�</h3>
 * <p></p>
 *
 * @author : TimVan
 * @date : 2021-04-15 14:30
 **/
class Solution {

    //    �������ְ������������ַ�: I�� V�� X�� L��C��D �� M��
//
//    �ַ�          ��ֵ
//    I             1
//    V             5
//    X             10
//    L             50
//    C             100
//    D             500
//    M             1000
//    ���磬 �������� 2 д�� II ����Ϊ�������е� 1��12 д�� XII ����Ϊ X + II �� 27 д��  XXVII, ��Ϊ XX + V + II ��
//
//    ͨ������£�����������С�������ڴ�����ֵ��ұߡ���Ҳ�������������� 4 ��д�� IIII������ IV������ 1 ������ 5 ����ߣ�����ʾ�������ڴ��� 5 ��С�� 1 �õ�����ֵ 4 ��ͬ���أ����� 9 ��ʾΪ IX���������Ĺ���ֻ�������������������
//
//    I ���Է��� V (5) �� X (10) ����ߣ�����ʾ 4 �� 9��
//    X ���Է��� L (50) �� C (100) ����ߣ�����ʾ 40 �� 90��
//    C ���Է��� D (500) �� M (1000) ����ߣ�����ʾ 400 �� 900��
//    ����һ���������֣�����ת��������������ȷ���� 1 �� 3999 �ķ�Χ�ڡ�

    public int romanToInt(String s) {

        int result = 0;
        int sLen = s.length();
        for (int i = 0; i < sLen; i++) {
            String currentSymbol = String.valueOf(s.charAt(i));
            //�ж��Ƿ���6���������֮һ
            if ((i + 1 < sLen) && getValue(currentSymbol + s.charAt(i + 1)) > 0) {
                currentSymbol = currentSymbol + s.charAt(i + 1);
                i++;
            }
            result += getValue(currentSymbol);
        }
        return result;
    }

    private int getValue(String ch) {
        switch (ch) {
            case "I":
                return 1;
            case "V":
                return 5;
            case "IV":
                return 4;
            case "IX":
                return 9;
            case "X":
                return 10;
            case "XL":
                return 40;
            case "XC":
                return 90;
            case "L":
                return 50;
            case "C":
                return 100;
            case "CD":
                return 400;
            case "CM":
                return 900;
            case "D":
                return 500;
            case "M":
                return 1000;
            default:
                return 0;
        }
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