class Solution {
    public void sortColors(int[] nums) {
        int[] buckets = new int[3];
        
        for(int num:nums){
            // count each number;
            buckets[num] += 1;
        }
        // fill each bucket in the original array 
        int i = 0;
        for(int n = 0; n < buckets.length; n++){
            for(int j = 0; j < buckets[n]; j++){
                nums[i] = n;
                i++;
            }
        }




    }
}