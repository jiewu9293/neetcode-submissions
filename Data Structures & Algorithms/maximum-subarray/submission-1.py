class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Maximum subarray sum ending at the current position
        current_sum = nums[0]

        # Maximum subarray sum found so far
        max_sum = nums[0]
        for num in nums[1:]:
            #each num we either extend the subarray or start a new one
            current_sum = max(num, current_sum + num)
            
            max_sum = max(current_sum,max_sum)
        return max_sum