// https://leetcode.com/problems/find-all-duplicates-in-an-array/

/*
* Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, 
return an array of all the integers that appears twice.
*/

class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        
        int i = 0;
        List <Integer> ans = new ArrayList<> ();
        while(i < nums.length) {
            int correct = nums[i] - 1;
            if(nums[i] != nums[correct]) {
                swap(nums, i, correct);
            } 
            else {
                i++;
            }
        }
        for(int index = 0; index < nums.length; index++) {
            if(nums[index] != index + 1) {
                ans.add(nums[index]);
            }
        }
        return ans;
        
    }
    
    static void swap(int[] arr, int first, int second) {
        int temp = arr[first];
        arr[first] = arr[second];
        arr[second] = temp;
    }
}
