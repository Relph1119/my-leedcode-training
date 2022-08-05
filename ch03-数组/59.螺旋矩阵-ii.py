#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        startx, starty = 0, 0
        loop = n // 2
        mid = n // 2
        count = 1

        for offset in range(1, loop + 1):
            for i in range(startx, n- offset):
                res[startx][i] = count
                count += 1
            
            for i in range(startx, n - offset):
                res[i][n-offset] = count
                count += 1
            
            for i in range(n - offset, starty, -1):
                res[n - offset][i] = count
                count += 1
            
            for i in range(n - offset, startx, -1):
                res[i][starty] = count
                count += 1

            startx += 1
            starty += 1

        if n % 2 != 0:
            res[mid][mid] = count

        return res 
# @lc code=end

