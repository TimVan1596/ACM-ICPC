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
    public static void test(boolean[] isUsed ){
        isUsed[0] = true;
    }


    public static void main(String[] args) {

        int n = 3;

        boolean[] isUsed = new boolean[n+1];
        Arrays.fill(isUsed,false);
//
//        for (int i = 1; i <= n; i++) {
//            isUsed[i] = true;
//
//            for (int j = 1; j <= n; j++) {
//                //跳过重复项
//                if (isUsed[j]){
//                    continue;
//                }
//                isUsed[j] = true;
//
//                for (int k = 1; k <= n; k++) {
//
//                    //跳过重复项
//                    if (isUsed[k]){
//                        continue;
//                    }
//
//                    System.out.print(i+"-"+j+"-"+k);
//                    System.out.println();
//
//                }
//
//                isUsed[j] = false;
//            }
//            isUsed[i] = false;
//
//        }

        test(isUsed);
        System.out.println(isUsed[0]);

    }
}
