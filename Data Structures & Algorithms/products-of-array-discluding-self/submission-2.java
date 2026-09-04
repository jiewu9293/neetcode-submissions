class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] res = new int[n];
        res[0] = 1;
        for(int i = 1; i < n; i++){
            res[i] = res[i-1] * nums[i-1];
        }
        // the first prefix product should be set to 1 cuz there is no value on the left hand side of the first position 
        //evaluate the prefix product at each position of the nums array
        //store the prefix product of each position in res array

        int postfix = 1;
        // the first postfix postfix should be set to 1 cuz there is no value on the right handside of the first position
        for(int i = n - 1; i >= 0; i--){ // start from the right handside of the res array, multiply each position by its corrsponding postfix product value
            res[i] *= postfix;
            postfix *= nums[i]; //after we get the next postfix product value we go to the next value in res array 
        } 
        return res;
    }
}  
