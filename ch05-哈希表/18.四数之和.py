# @before-stub-for-debug-begin
from python3problem18 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()
        for k in range(n):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            for i in range(k+1, n):
                if i > k + 1 and nums[i] == nums[i - 1]:
                    continue
                left = i + 1
                right = n - 1

                while left < right:
                    if nums[k] + nums[i] + nums[left] + nums[right] > target:
                        right -= 1
                    elif nums[k] + nums[i] + nums[left] + nums[right] < target:
                        left += 1
                    else:
                        result.append([nums[k], nums[i], nums[left], nums[right]])
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        right -= 1
                        left += 1
                
        return result
# @lc code=end

