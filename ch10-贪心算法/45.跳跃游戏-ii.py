#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        cur_dist = 0
        ans = 0
        next_dist = 0
        for i in range(len(nums) - 1):
            next_dist = max(nums[i] + i, next_dist)
            if i == cur_dist:
                ans += 1
                cur_dist = next_dist
        
        return ans
# @lc code=end

