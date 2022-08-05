#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(candidates, target, sum, start_index):
            if sum > target:
                return 
            
            if sum == target:
                result.append(path.copy())
                return
            
            for i in range(start_index, len(candidates)):
                sum += candidates[i]
                path.append(candidates[i])
                backtracking(candidates, target, sum, i)
                sum -= candidates[i]
                path.pop()

        path = []
        result = []
        backtracking(candidates, target, 0, 0)
        return result
# @lc code=end

