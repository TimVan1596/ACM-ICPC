package com.timvan.Algorithm.Trick.LC0414;

/**
 * <h3>���ű�</h3>
 * <p></p>
 *
 * @author : TimVan
 * @date : 2021-04-14 16:31
 **/
class Solution {

//    ����һ������ x ����� x ��һ���������������� true �����򣬷��� false ��
//
//    ��������ָ���򣨴������ң��͵��򣨴������󣩶�����һ�������������磬121 �ǻ��ģ��� 123 ���ǡ�
//
//            ?
//
//    ʾ�� 1��
//
//    ���룺x = 121
//    �����true
//    ʾ��?2��
//
//    ���룺x = -121
//    �����false
//    ���ͣ��������Ҷ�, Ϊ -121 �� ���������, Ϊ 121- �����������һ����������
//    ʾ�� 3��
//
//    ���룺x = 10
//    �����false
//    ���ͣ����������, Ϊ 01 �����������һ����������
//    ʾ�� 4��
//
//    ���룺x = -101
//    �����false
//
//    ��ʾ��
//
//    ���ף����ܲ�������תΪ�ַ�����������������


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