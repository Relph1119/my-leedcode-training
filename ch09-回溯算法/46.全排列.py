#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrackng(nums, used):
            if len(path) == len(nums):
                result.append(path.copy())
                return 

            for i in range(len(nums)):
                if used[i] == True:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrackng(nums, used)
                path.pop()
                used[i] = False

        result = []
        path = []
        used = [False] * len(nums)
        backtrackng(nums, used)
        return result

# @lc code=end

