#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def is_valid(self, row, col, val, board):
        for i in range(9):
            if board[row][i] == val:
                return False

        for j in range(9):
            if board[j][col] == val:
                return False
        
        start_row = row // 3 * 3
        start_col = col // 3 * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == val:
                    return False
        
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtracking(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] != '.':
                        continue
                    for k in [str(s) for s in range(1, 10)]:
                        if self.is_valid(i, j, k, board):
                            board[i][j] = k
                            if backtracking(board):
                                return True
                            board[i][j] = '.'
        
                    return False
        
            return True
        
        backtracking(board)
# @lc code=end

