#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)

        if size == 0:
            return 0

        dp = [[0] * 4 for _ in range(size)]

        dp[0][0] = -prices[0]

        for i in range(1, size):
            # 0: 买入股票
            # 1：度过冷冻期，已卖出股票
            # 2：卖出股票
            # 3：冷冻期
            dp[i][0] = max(dp[i - 1][0], max(dp[i - 1][3], dp[i - 1][1]) - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][3])
            dp[i][2] = dp[i - 1][0] + prices[i]
            dp[i][3] = dp[i - 1][2]

        return max(dp[size - 1][3], dp[size - 1][1], dp[size - 1][2])
# @lc code=end

