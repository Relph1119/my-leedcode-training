#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtracking(nums, used):
            if len(path) == len(nums):
                result.append(path.copy())
                return 
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtracking(nums, used)
                    path.pop()
                    used[i] = False

        if not nums:
            return []
        result = []
        path = []
        used = [False] * len(nums)
        nums.sort()
        backtracking(nums, used)
        return result
# @lc code=end

