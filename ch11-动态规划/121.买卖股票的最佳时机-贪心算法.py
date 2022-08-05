#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        result = 0
        for i in range(len(prices)):
            low = min(low, prices[i])
            result = max(result, prices[i] - low)
        
        return result
# @lc code=end

