#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow_index, fast_index = 0, 0
        while fast_index < len(nums):
            if val != nums[fast_index]:
                nums[slow_index] = nums[fast_index]
                slow_index += 1
            fast_index += 1
        
        return slow_index
# @lc code=end

