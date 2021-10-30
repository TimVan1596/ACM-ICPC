package com.timvan.Algorithm.Trick.LC0413;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        //定义一个哈希表，key是数组的值，value是下标
        Map<Integer, Integer> arrayMap = new HashMap<>();
        int numsLength = nums.length;
        for (int i = 0; i < numsLength; i++) {
            result[1] = i;
            int firstNum = nums[i];
            //若在已有的hash标存在则结束
            if (arrayMap.containsKey(target - firstNum)) {
                result[0] = arrayMap.get(target - firstNum);
                break;
            }
            //不存在则添加键值对
            else if (!arrayMap.containsKey(firstNum)) {
                arrayMap.put(nums[i], i);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        int[] nums = {2,7,11,15};
        int target = 9;
        System.out.println(Arrays.toString(new Solution()
                .twoSum(nums, target)));


    }
}
