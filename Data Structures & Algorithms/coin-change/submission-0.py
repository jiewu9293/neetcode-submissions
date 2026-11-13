class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        unreachable = float("inf")
        dp = [unreachable] * (amount + 1)
        
        dp[0] = 0
        for x in range(1, amount + 1):
            for coin in coins:
                 if coin <= x:
                    candidate = dp[x - coin] + 1
                    dp[x] = min(candidate,dp[x])
        if dp[amount] == unreachable:
            return -1 
        else:
            return dp[amount]


        

            