class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 0; // slow pointer
        for(int j =1 ; j< nums.length; j++){ // j is the fast pointer
            if(nums[j] != nums[i]){
                i++;
                nums[i] = nums[j];
            }
        }
        return i + 1; // number of unique elements 
    }               // i point to the last unique element 
}