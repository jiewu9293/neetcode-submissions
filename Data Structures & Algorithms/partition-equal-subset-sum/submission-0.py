class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = True

        for i,num in enumerate(nums,start=1):
            for s in range(target + 1):
                dp[i][s] = dp[i-1][s]
                if s >= num:
                    dp[i][s] = dp[i-1][s] or dp[i-1][s-num]
        return dp[len(nums)][target]



