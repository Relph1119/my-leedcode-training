#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        size = len(prices)
        
        if len(prices) == 0:
            return 0

        dp = [[0] * (2 * k + 1) for _ in range(size)]

        j = 1
        while j < 2 * k:
            dp[0][j] = -prices[0]
            j += 2

        for i in range(1, size):
            j = 0
            while j < 2 * k - 1:
                dp[i][j + 1] = max(dp[i - 1][j + 1], dp[i - 1][j] - prices[i])
                dp[i][j + 2] = max(dp[i - 1][j + 2], dp[i - 1][j + 1] + prices[i])
                j += 2

        return dp[size - 1][2 * k]
# @lc code=end

