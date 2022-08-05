#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(n, k, start_index):
            if len(path) == k:
                result.append(path.copy())
                return

            for i in range(start_index, n + 1):
                path.append(i)
                backtracking(n, k, i + 1)
                path.pop()                

        path = []
        result = []
        backtracking(n, k, 1)
        return result
# @lc code=end

