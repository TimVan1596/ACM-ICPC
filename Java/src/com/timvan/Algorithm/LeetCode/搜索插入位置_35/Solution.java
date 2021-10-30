package com.timvan.Algorithm.LeetCode.搜索插入位置_35;

/**
 * <h3>蓝桥杯</h3>
 * <p></p>
 *
 * @author : TimVan
 * @date : 2021-04-26 15:58
 **/
class Solution {

//    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
//
//    你可以假设数组中无重复元素。
//
//    示例 1:
//
//    输入: [1,3,5,6], 5
//    输出: 2
//
//    示例 2:
//
//    输入: [1,3,5,6], 2
//    输出: 1
//    示例 3:
//
//    输入: [1,3,5,6], 7
//    输出: 4

    public int searchInsert(int[] nums, int target) {
        int numsLength = nums.length;
        //极端情况判断
        if (numsLength <= 0) {
            return 0;
        }
        if (numsLength == 1 && target < nums[0]) {
            return 0;
        }
        for (int i = 0; i < numsLength; i++) {
            if (nums[i] >= target) {
                return i;
            }
        }
        return numsLength;
    }

    public static void main(String[] args) {
        int[] nums = {1, 3, 5, 6};
        int target = 5;
        System.out.println(new Solution().searchInsert(nums, target));
        target = 2;
        System.out.println(new Solution().searchInsert(nums, target));
        nums = new int[0];
        System.out.println(new Solution().searchInsert(nums, target));
        nums = new int[]{1};
        System.out.println(new Solution().searchInsert(nums, target));
        nums = new int[]{2};
        System.out.println(new Solution().searchInsert(nums, target));
        nums = new int[]{3};
        System.out.println(new Solution().searchInsert(nums, target));
    }
}