#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def is_valid(self, row, col, chessbord, n):
        for i in range(row):
            if chessbord[i][col] == 'Q':
                return False
        
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if chessbord[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        i = row - 1
        j = col + 1
        while i >=0 and j < n:
            if chessbord[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True

    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtracking(n, row, chessbord):
            if row == n:
                temp_res = []
                for temp in chessbord:
                    temp_str = "".join(temp)
                    temp_res.append(temp_str)
                result.append(temp_res)
            
            for col in range(n):
                if self.is_valid(row, col, chessbord, n):
                    chessbord[row][col] = 'Q'
                    backtracking(n, row+1, chessbord)
                    chessbord[row][col] = '.'

        if not n:
            return []
        result = []
        chessbord = [['.'] * n for _ in range(n)]
        backtracking(n, 0, chessbord)
        return result
# @lc code=end

