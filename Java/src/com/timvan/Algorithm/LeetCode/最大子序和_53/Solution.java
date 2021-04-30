package com.timvan.Algorithm.LeetCode.最大子序和_53;

/**
 * <h3>蓝桥杯</h3>
 * <p></p>
 *
 * @author : TimVan
 * @date : 2021-04-28 14:08
 **/
class Solution {
    //    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
//    示例 1：
//    输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
//    输出：6
//    解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
//
//    示例 2：
//    输入：nums = [1]
//    输出：1
    public int maxSubArray(int[] nums) {
        int numsLength = nums.length;
        // 上三角判断，比如从[0~1]，[0~2],[0~3]来判断
        int max = nums[0];
        for (int i = 0; i < numsLength; i++) {
            // current=当前待加入的数字，previousValue = 之前[0~i]的总和
            int current = nums[i];
            int previousValue = current;
            // 因为首个必须要添加，不考虑正负
            if (max < current) {
                max = current;
            }
            for (int j = i + 1; j < numsLength; j++) {
                current = previousValue + nums[j];
                previousValue = current;
                if (current > 0 && (max < current)) {
                    max = current;
                }
            }
        }
        return max;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        System.out.println(solution.maxSubArray(nums));
        nums = new int[]{1};
        System.out.println(solution.maxSubArray(nums));
        nums = new int[]{0};
        System.out.println(solution.maxSubArray(nums));
        nums = new int[]{-1};
        System.out.println(solution.maxSubArray(nums));
        nums = new int[]{-100000};
        System.out.println(solution.maxSubArray(nums));
        nums = new int[]{-2, -1};
        System.out.println(solution.maxSubArray(nums));

    }
}