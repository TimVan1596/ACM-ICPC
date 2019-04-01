package com.timvan.算法训练.数据结构.第一讲;

/**
 * 1.3 应用实例：最大子列和问题（3节共20:02）
 * https://mooc.study.163.com/learn/1000033001?tid=2402970002#/learn/content?type=detail&id=2403307439&cid=2403323313
 *
 * @author TimVan on 2019/3/26
 */
public class 最大连续子数列和 {

//    给定一个数列，其中可能有正数也可能有负数，找出其中连续的一个子数列（不允许空数列），使它们的和尽可能大。
//    输入：
//            8
//            -2 6 -1 5 4 -7 2 3
//    输出：
//            14

    public static void main(String[] args) {
        //输入数组
        int N = 8;
        int[] arr = {-2,6,-1,5,4,-7,2,3};


        int max = arr[0];
        for (int i = 0; i < N; i++) {

            int sum = 0;
            for (int j = i; j < N ; j++) {
                sum += arr[j];
                if(sum > max ){
                    max = sum;
                }
            }

        }

        System.out.println(max);

    }
}
