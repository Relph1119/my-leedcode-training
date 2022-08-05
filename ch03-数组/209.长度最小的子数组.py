#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = len(nums) + 1
        sum = 0
        i = j = 0
        for j in range(len(nums)):
            sum += nums[j]
            while sum >= target:
                result = min(result, j - i + 1)
                sum -= nums[i]
                i += 1

        return 0 if result == len(nums) + 1 else result
# @lc code=end

