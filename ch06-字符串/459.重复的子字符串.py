#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution:
    def get_next(self, next, s):
        j = 0
        next[0] = j
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
            next[i] = j

    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 0:
            return 0

        next = [0 for _ in range(len(s))]
        self.get_next(next, s)
        slen = len(s)
        if next[slen - 1] != 0 and (slen % (slen - next[slen - 1]) == 0):
            return True
        return False

# @lc code=end

