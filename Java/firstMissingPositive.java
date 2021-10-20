// https://leetcode.com/problems/first-missing-positive/

/*
* Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

Input: nums = [1,2,0]
Output: 3
*/

class Solution {
    public int firstMissingPositive(int[] nums) {
        
        int i = 0;
        while(i < nums.length) {
            int correct = nums[i] - 1;
            if(nums[i] > 0 && nums[i] <= nums.length && nums[i] != nums[correct]) {
                swap(nums, i, correct);
            }
            else {
                i++;
            }
        }
        
        for(int index = 0; index < nums.length; index++) {
            if(nums[index] != index + 1) {
                return index + 1;
            }
        }
        
        return nums.length + 1;
        
    }
    
    static void swap(int[] arr, int f, int l) {
        int temp = arr[f];
        arr[f] = arr[l];
        arr[l] = temp;
    }
}
