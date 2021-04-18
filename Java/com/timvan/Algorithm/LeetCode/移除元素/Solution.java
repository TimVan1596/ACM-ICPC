package com.timvan.Algorithm.LeetCode.移除元素;

class Solution {
    public int removeElement(int[] nums, int val) {
        int currIndex = 0;
        if (nums.length <= 0){
            return 0;
        }
        int numsLength = nums.length;
        for (int i = 0; i < numsLength; i++) {
            if (nums[i]!=val){
                nums[currIndex] = nums[i];
                currIndex++;
            }
        }
        return currIndex;
    }

    public static void main(String[] args) {
        //nums = [0,1,2,2,3,0,4,2], val = 2
        int[] nums = {0,1,2,2,3,0,4,2};
        int val = 2;
        int len =  new Solution().removeElement(nums,val);
        System.out.println(len);
        for (int i = 0; i < len; i++) {
            System.out.println(nums[i]);
        }

    }
}