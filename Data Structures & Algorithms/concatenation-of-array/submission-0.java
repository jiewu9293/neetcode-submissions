class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length; // length of the array
        int[] ans = new int[2*n]; // initialised an array size if double the input array

        for(int i = 0; i< n; i++){
            ans[i] = nums[i];// assign value to the first partition of the ans[]
            ans[i+n] = nums[i];//assign value to the second partition of the ans[]
        }
        return ans;
    }
}