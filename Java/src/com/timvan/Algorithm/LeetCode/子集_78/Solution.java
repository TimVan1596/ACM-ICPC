package com.timvan.Algorithm.LeetCode.子集_78;

import java.util.LinkedList;
import java.util.List;
import java.util.Stack;
import java.util.concurrent.ForkJoinPool;

/**
 * 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
 * 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
 * <p>
 * 示例 1：
 * 输入：nums = [1,2,3]
 * 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
 * 示例 2：
 * 输入：nums = [0]
 * 输出：[[],[0]]
 **/
public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> subList = new LinkedList<>();
        subList.add(new LinkedList<>());
        // 原理：{[]}中各元素添加1再加上原来,成{[],[1]}，循环往复
        for (int num :nums) {
            //cacheList相当于对subList的深度拷贝，否则会修改引用
            List<List<Integer>> cacheList = new LinkedList<>();
            for (List<Integer> singleList:subList) {
                List<Integer> cacheSingleList = new LinkedList<>(singleList);
                cacheSingleList.add(num);
                cacheList.add(cacheSingleList);
            }
            subList.addAll(cacheList);
        }
        return subList;
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3};
        List<List<Integer>> subList = new Solution().subsets(nums);
        System.out.println(subList);
        nums = new int[]{0};
        subList = new Solution().subsets(nums);
        System.out.println(subList);
    }
}
