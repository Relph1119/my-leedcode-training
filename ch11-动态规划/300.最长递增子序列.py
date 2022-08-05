#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        if size <= 1:
            return size
        dp = [1] * size

        result = 0
        for i in range(1, size):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            result = max(dp[i], result)

        return result
# @lc code=end

