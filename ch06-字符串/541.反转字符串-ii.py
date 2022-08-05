#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        p = 0
        while p < len(s):
            s = s[:p] + s[p:p + k][::-1] + s[p + k:]
            p = p + 2 * k
        return s
# @lc code=end

