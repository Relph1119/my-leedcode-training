#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                word = s[j:i]
                if word in wordDict and dp[j]:
                    dp[i] = True
        
        return dp[len(s)]
# @lc code=end

