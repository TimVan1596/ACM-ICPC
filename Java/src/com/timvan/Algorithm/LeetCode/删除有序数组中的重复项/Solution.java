package com.timvan.Algorithm.LeetCode.删除有序数组中的重复项;

import java.util.ArrayList;

/**
 * <h3>蓝桥杯</h3>
 * <p></p>
 *
 * @author : TimVan
 * @date : 2021-04-16 16:04
 **/
class Solution {
    public int removeDuplicates(int[] nums) {
        int currentIndex = 0;
        if (nums.length <= 1) {
            return nums.length;
        }
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[currentIndex]) {
                currentIndex++;
                nums[currentIndex] = nums[i];
            }
        }
        return currentIndex + 1;
    }

    public static void main(String[] args) {
        int[] nums = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
        int all = new Solution().removeDuplicates(nums);
        System.out.println(all);
        for (int i = 0; i < all; ++i) {
            System.out.println(nums[i]);
        }
    }
}