#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(candidates, target, sum_, start_index):            
            if sum_ == target:
                result.append(path.copy())
                return
            
            for i in range(start_index, len(candidates)):
                if sum_ + candidates[i] > target:
                    return
            
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue

                sum_ += candidates[i]
                path.append(candidates[i])
                backtracking(candidates, target, sum_, i + 1)
                sum_ -= candidates[i]
                path.pop()

        result = []
        path = []
        candidates.sort()
        backtracking(candidates, target, 0, 0)
        return result
# @lc code=end

