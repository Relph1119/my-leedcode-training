#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        size = len(height)

        max_left = [0] * size
        max_left[0] = height[0]
        for i in range(size):
            max_left[i] = max(max_left[i - 1], height[i])

        max_right = [0] * size
        max_right[-1] = height[-1]
        for i in range(size-2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])
        
        sum = 0
        for i in range(size):
            h = min(max_left[i], max_right[i]) - height[i]
            if h > 0:
                sum += h
        
        return sum 
# @lc code=end

