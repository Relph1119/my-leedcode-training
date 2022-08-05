#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
from operator import le


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + int((right - left) / 2)
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        
        return -1
# @lc code=end

