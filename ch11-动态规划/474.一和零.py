#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#

# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for str in strs:
            one_num, zero_num = 0, 0
            for c in str:
                if int(c) == 0:
                    zero_num += 1
                else:
                    one_num += 1
            
            for i in range(m, zero_num - 1, -1):
                for j in range(n, one_num - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zero_num][j - one_num] + 1)

        return dp[m][n]

# @lc code=end

