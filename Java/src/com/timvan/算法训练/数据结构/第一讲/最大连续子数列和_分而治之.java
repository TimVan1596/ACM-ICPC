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

    static private int contiSum(int[] arr , int left , int right) {

        printArr(arr,left,right);

        if(left == right){
            return arr[left];
        }

        //分而治之的中间点
        int mid = left + ( right >> 1 );

        //先计算左右两边（递归进行）
        int leftMax = contiSum(arr,left,mid);
        int rightMax = contiSum(arr,mid+1,right);


        //计算跨中间的第三种情况
        int leftSubSum = 0 , leftSubMax = 0;
        for (int i = mid ; i >= left ; i--) {
            leftSubSum += arr[i];
            if( leftSubSum > leftSubMax ){
                leftSubMax = leftSubSum;
            }
        }

        int rightSubSum = 0 , rightSubMax = 0;
        for (int i = mid+1; i <= right ; i++) {
            rightSubSum += arr[i];
            if( rightSubSum > rightSubMax ){
                rightSubMax = rightSubSum;
            }
        }


        int crossMax = leftSubMax + rightSubMax;


        return  Math.max(Math.max(rightMax,leftMax),crossMax) ;
    }

    //打印数组
    static void printArr(int[] arr,int left, int right)
    {
        System.out.print("l:"+left+" r:"+right+" arr: ");
        for (int i = left ; i  <= right ; ++i){
            System.out.print(arr[i]+",");
        }

        //序列长度为1时
        if(left == right){
            System.out.print("RET  "+arr[left]);
        }

        System.out.println();
    }



    public static void main(String[] args) {
        //输入数组
        int N = 8;
        int[] arr = {-2, 6, -1, 5, 4, -7, 2, 3};


        System.out.println(contiSum(arr,0,arr.length-1));

//        System.out.println(contiSum(arr));

    }
}
