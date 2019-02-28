package com.timvan.算法训练;

import java.util.ArrayList;
import java.util.Scanner;

/**
 * @description: 调整每组数的排列顺序，使得两组数据相同下标元素对应相乘，然后相加的和最小
 * @author: Tim Van
 * @create: 2019-02-27 01:24
 **/
public class 算法训练_最小乘积基本型 {

//    问题描述
//　　给两组数，各n个。
//            　　请调整每组数的排列顺序，使得两组数据相同下标元素对应相乘，然后相加的和最小。要求程序输出这个最小值。
//            　　例如两组数分别为:1 3　　-5和-2 4 1
//
//            　　那么对应乘积取和的最小值应为：
//            　　(-5) * 4 + 3 * (-2) + 1 * 1 = -25
//    输入格式
//　　第一个行一个数T表示数据组数。后面每组数据，先读入一个n，接下来两行每行n个数，每个数的绝对值小于等于1000。
//            　　n<=8,T<=1000
//    输出格式
//　　一个数表示答案。


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();

        for (int i = 0; i < T; i++) {
            int n = scanner.nextInt();
            int[] arr1 = new int[n],arr2 = new int[n];

            //输入第一列数
            for (int k = 0; k < n; k++) {
                arr1[k] = scanner.nextInt();
            }

            //输入第二列数
            for (int k = 0; k < n; k++) {
                arr2[k] = scanner.nextInt();
            }

            int sum = 0;
            for (int j = 0; j < n; j++) {
                sum += (arr1[j]*arr2[j]);
            }

            System.out.println("sum = "+sum);

        }

    }
}
