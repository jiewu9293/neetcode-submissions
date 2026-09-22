class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #max_sum = total_sum - min_sum
        #Initialize all states with the first element
        total_sum = nums[0]

        # Maximum subarray states
        max_ending_here = nums[0]
        max_sum = nums[0]

        # Minimum subarray states
        min_ending_here = nums[0]
        min_sum = nums[0]
        for num in nums[1:]:
            #extend subarray
            max_ending_here = max(num, max_ending_here + num)
            max_sum = max(max_sum, max_ending_here)

            min_ending_here = min(num, min_ending_here + num)
            min_sum = min(min_sum, min_ending_here)

            total_sum += num    

        # If all numbers are negative, the circular result would
        if max_sum < 0:
            return max_sum
        # Case 1: Non-circular maximum subarray
        # Case 2: Circular maximum subarray
        return max(max_sum, total_sum - min_sum)
