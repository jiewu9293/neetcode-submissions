class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, length = 0, float('inf')
        total = 0
        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                length = min(length,R - l + 1)
                total -= nums[l]
                l += 1
        return 0 if length == float('inf') else length