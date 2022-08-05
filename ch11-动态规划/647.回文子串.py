#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        dp = [[False] * size for _ in range(size)]
        result = 0
        for i in range(size - 1, -1, -1):
            for j in range(i, size):
                if s[i] == s[j]:
                    if j - i <= 1:
                        result += 1
                        dp[i][j] = True
                    elif dp[i + 1][j - 1]:
                        result += 1
                        dp[i][j] = True
        
        return result

# @lc code=end

