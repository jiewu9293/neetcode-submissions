class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        cols = len(obstacleGrid[0])
        dp = [0] * cols
        dp[0] = 1
        for row in obstacleGrid:
            for col in range(cols):
                if row[col] == 1:
                    dp[col] = 0

                elif col > 0:
                     dp[col] += dp[col - 1]
        return dp[cols-1]