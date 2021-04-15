package com.timvan.Algorithm.Trick.LC0414.������ת;

import static java.lang.Math.pow;

/**
 * <h3>���ű�</h3>
 * <p>7. ������ת</p>
 *
 * @author : TimVan
 * @date : 2021-04-14 15:53
 **/
public class Solution {
//    ����һ�� 32 λ���з������� x �����ؽ� x �е����ֲ��ַ�ת��Ľ����
//    �����ת���������� 32 λ���з��������ķ�Χ [?231,  231 ? 1] ���ͷ��� 0��

//    ���軷��������洢 64 λ�������з��Ż��޷��ţ���
//    ʾ�� 1��
//    ���룺x = 123
//    �����321
//    ʾ�� 2��
//
//    ���룺x = -123
//    �����-321
//    ʾ�� 3��
//
//    ���룺x = 120
//    �����21
//    ʾ�� 4��
//
//    ���룺x = 0
//    �����0
//             
//    ��ʾ��
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
