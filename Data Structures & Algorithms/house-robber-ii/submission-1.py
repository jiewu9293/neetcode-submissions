class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        def helper(houses):
            n = len(houses)
            dp = [0] * (n + 1)
            dp[1] = houses[0]

            for i in range(2,n+1):
                skip_current = dp[i-1]

                rob_current = houses[i-1] + dp[i-2]

                dp[i] = max(skip_current,rob_current)
            return dp[n]

        best_without_last = nums[:-1]
        best_without_first = nums[1:]
        return max(helper(best_without_last),helper(best_without_first))



            