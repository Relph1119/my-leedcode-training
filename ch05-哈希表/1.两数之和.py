#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()
        for idx, val in enumerate(nums):
            if target - val not in records:
                records[val] = idx
            else:
                return [records[target - val], idx]
# @lc code=end

