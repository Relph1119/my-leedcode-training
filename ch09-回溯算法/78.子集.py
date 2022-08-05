#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtracking(nums, start_index):
            result.append(path.copy())
            if start_index >= len(nums):
                return 
            
            for i in range(start_index, len(nums)):
                path.append(nums[i])
                backtracking(nums, i + 1)
                path.pop()


        result = []
        path = []
        backtracking(nums, 0)
        return result
# @lc code=end

