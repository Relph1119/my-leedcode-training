#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtracking(nums, start_index, used):
            result.append(path.copy())
            for i in range(start_index, len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == False:
                    continue
                path.append(nums[i])
                used[i] = True
                backtracking(nums, i + 1, used)
                used[i] = False
                path.pop()

        result = []
        path = []
        used = [False] * len(nums)
        nums.sort()
        backtracking(nums, 0, used)
        return result
# @lc code=end

  