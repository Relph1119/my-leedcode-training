#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow +=1
            fast += 1
        return slow

# @lc code=end

