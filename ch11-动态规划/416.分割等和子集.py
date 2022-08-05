# @before-stub-for-debug-begin
from python3problem416 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_value = sum(nums)
        if sum_value % 2 == 1:
            return False
        target = sum_value // 2

        dp = [0] * (target + 1)

        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
            
        if dp[target] == target:
            return True
        
        return False
# @lc code=end

