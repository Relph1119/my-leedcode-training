#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        i = 0
        while i < m and obstacleGrid[i][0] == 0:
            dp[i][0] = 1
            i += 1

        j = 0
        while j < n and obstacleGrid[0][j] == 0:
            dp[0][j] = 1
            j += 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue

                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        
        return dp[m - 1][n - 1]
# @lc code=end

