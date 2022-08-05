#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#

# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtracking(nums, start_index):
            if len(path) > 1:
                result.append(path.copy())

            uset = set()
            for i in range(start_index, len(nums)):
                if (path and nums[i] < path[-1]) or nums[i] in uset:
                    continue

                uset.add(nums[i])
                path.append(nums[i])
                backtracking(nums, i + 1)
                path.pop()

        result = []
        path = []
        backtracking(nums, 0)
        return result
# @lc code=end

