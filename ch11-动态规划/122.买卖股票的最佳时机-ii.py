#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size == 0:
            return 0
        dp = [[0] * 2 for _ in range(size)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, size):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        
        return dp[size - 1][1]
# @lc code=end

