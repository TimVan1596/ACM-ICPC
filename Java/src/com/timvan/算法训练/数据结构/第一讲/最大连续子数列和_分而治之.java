package com.timvan.算法训练.数据结构.第一讲;

/**
 * 1.3 应用实例：最大子列和问题（3节共20:02）
 * https://mooc.study.163.com/learn/1000033001?tid=2402970002#/learn/content?type=detail&id=2403307439&cid=2403323313
 *
 * @author TimVan on 2019/3/26
 */
public class 最大连续子数列和_分而治之 {

//    给定一个数列，其中可能有正数也可能有负数，找出其中连续的一个子数列（不允许空数列），使它们的和尽可能大。
//    输入：
//            8
//            -2 6 -1 5 4 -7 2 3
//    输出：
//            14

    static int contiSum(int[] arr) {
        int max = arr[0];

        //分而治之的中间点
        int mid = arr.length / 2;

        int leftSum = 0, leftMax = 0;
        for (int i = 0 ; i <  mid; i++) {
            leftSum += arr[i];
            if (leftSum > leftMax) {
                leftMax = leftSum;
            }
        }

//        int leftSum = 0 , leftMax = 0;
//        for (int i = mid-1 ; i >= 0 ; i--) {
//            leftSum += arr[i];
//            if( leftSum > leftMax ){
//                leftMax = leftSum;
//            }
//        }
//
//        int rightSum = 0 , rightMax = 0;
//        for (int i = mid; i < arr.length ; i++) {
//            rightSum += arr[i];
//            if( rightSum > rightMax ){
//                rightMax = rightSum;
//            }
//        }
//
//        int crossMax = rightMax + leftMax;
//
//
//        System.out.println("rightMax = "+rightMax);
//        System.out.println("leftMax = "+leftMax);
//        System.out.println("crossMax = "+crossMax);
//
//        for (int i = 0; i < arr.length; i++) {
//
//            int sum = 0;
//            for (int j = i; j < arr.length ; j++) {
//                sum += arr[j];
//                if(sum > max ){
//                    max = sum;
//                }
//            }
//
//        }

        return max;
    }

    static int solve(int[] num,int left, int right)
    {
        //序列长度为1时
        if(left == right){
            return num[left];
        }

        //划分为两个规模更小的问题
        int mid = left + right >> 1;
        int lans = solve(num,left, mid);
        int rans = solve(num,mid + 1, right);

        //横跨分割点的情况
        int sum = 0, lmax = num[mid], rmax = num[mid + 1];
        for(int i = mid; i >= left; i--) {
            sum += num[i];
            if(sum > lmax){
                lmax = sum;
            }
        }
        sum = 0;
        for(int i = mid + 1; i <= right; i++) {
            sum += num[i];
            if(sum > rmax){
                rmax = sum;
            }
        }

        //答案是三种情况的最大值
        int ans = lmax + rmax;
        if(lans > ans) {
            ans = lans;
        }
        if(rans > ans) {
            ans = rans;
        }

        return ans;
    }


    public static void main(String[] args) {
        //输入数组
        int N = 8;
        int[] arr = {-2, 6, -1, 5, 4, -7, 2, 3};


        System.out.println(solve(arr,0,arr.length-1));

//        System.out.println(contiSum(arr));

    }
}
