package com.timvan.Java方向班.程序逻辑练习0218;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * @author TimVan
 * @date 2019/2/18 10:53
 */
public class One_四整数从大到小排序 {
    public static void main(String[] args) {
        int arr[] = {10,55,20,19};
        List<Integer> arrList = new ArrayList();

        for (int a :arr) {
            arrList.add(a);
        }
        //调用排序算法
        Collections.sort(arrList);

        //判断是否是第一个数
        boolean isFirst = true;
        for (int a : arrList) {
            if (isFirst){
                isFirst = false;
                System.out.print(a);
            }
            else{
                System.out.print(","+a);
            }
        }
    }
}
