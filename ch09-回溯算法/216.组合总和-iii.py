#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
from unittest import result


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtracking(targetSum, k, sum, start_index):
            # 终止条件
            if sum > targetSum:
                return

            if len(path) == k:
                if sum == targetSum:
                    result.append(path.copy())
                return
            
            # 遍历回溯
            for i in range(start_index, 9 - (k - len(path)) + 2):
                sum += i
                path.append(i)
                backtracking(targetSum, k, sum, i+1)
                sum -= i
                path.pop()

        path = []
        result = []
        backtracking(n, k, 0, 1)
        return result
# @lc code=end

