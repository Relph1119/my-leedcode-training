#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:

    def partition(self, s: str) -> List[List[str]]:
        def backtracking(s, start_index):
            if start_index >= len(s):
                result.append(path.copy())
                return
            
            for i in range(start_index, len(s)):
                temp = s[start_index: i+1]
                if temp == temp[::-1]:
                    path.append(temp)
                    backtracking(s, i + 1)
                    path.pop()       

        result = []
        path = []
        backtracking(s, 0)
        return result
# @lc code=end

