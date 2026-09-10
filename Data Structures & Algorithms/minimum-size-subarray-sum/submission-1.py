class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #window_sum < target expand window
        #winodow_sum >= target reduce window update window length
        left = 0
        window_sum = 0
        min_length = float("inf")
        for right in range(len(nums)):
            #add to window
            window_sum += nums[right]
            #when window is valid reduce window
            while window_sum >= target:
                current_length = right - left + 1 
                min_length = min(min_length,current_length)
                #remove leftmost num from window
                window_sum -= nums[left]
                left += 1
        # if min_length not update means such subarray not exists return 0 
        return 0 if min_length == float("inf") else min_length
            