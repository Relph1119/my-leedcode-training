#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        
        result = 1
        dp = [1] * size
        for i in range(size - 1):
            if nums[i + 1] > nums[i]:
                dp[i + 1] = dp[i] + 1
            
            if dp[i + 1] > result:
                result = dp[i + 1]
        
        return result 
# @lc code=end

