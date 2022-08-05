#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        
        dp = [0] * size
        dp[0] = nums[0]
        for i in range(1, size):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])

        return max(dp)
# @lc code=end

