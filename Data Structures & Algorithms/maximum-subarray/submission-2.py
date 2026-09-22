class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Maximum subarray sum ending at the current position
        current_sum = nums[0]

        # Maximum subarray sum found so far
        max_sum = nums[0]
        for i in range(1,len(nums)):
            #each num we either extend the subarray or start a new one
            current_sum = max(nums[i], current_sum + nums[i])
            
            max_sum = max(current_sum,max_sum)
        return max_sum