class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> prev = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            int diff = target - nums[i];

            if(prev.containsKey(diff)){
                return new int[]{prev.get(diff),i};
            }
            prev.put(nums[i],i);

        }
        return new int[]{} ;// if after iteration we did't find two number in the array that sum up to the target 
         // then we simply return empty array, indicate that no answer found 
    }
}
