package com.timvan.技巧;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.zip.Deflater;

/**
 * @description: 全排列排序（字典序）
 * @author: Tim Van
 * @create: 2019-03-08 00:35
 **/
public class 全排列 {

    /**
     * cnt = 全排列个数
     */
    static private int cnt = 0;

    /**
     * 交换
     */
    private static void arrSwap(int[] arr, int first, int second) {
        int c = arr[first];
        arr[first] = arr[second];
        arr[second] = c;
    }

    /**
     * 打印数组
     */
    private static void printArr(int[] arr) {

        for (int i = 0; i < arr.length; i++) {
            if ( i == 0){
                System.out.print(arr[i]);
            }
            else{
                System.out.print("," + arr[i]);
            }
        }

        System.out.println();
    }

    /**
     * 对数组进行全排列
     * perm = permutation
     */
    private static void perm(int[] arr,int start ,int end){
        //迭代终止条件
        if (start == end){
            //增加一次
            cnt++;
            printArr(arr);
        }
        else{

            for (int i = start; i <= end; i++) {
                if (start != i){
                    arrSwap(arr,start,i);
                }
                perm(arr,start+1,end);
                if (start != i){
                    arrSwap(arr,start,i);
                }
            }
        }


    }


    public static void main(String[] args) {

        int n = 3;
        int arr[] = {1, 2, 3, 4};
        perm(arr,0,arr.length-1);
        System.out.println(arr.length+"个数进行排列有"+cnt+"种情况");
    }
}
