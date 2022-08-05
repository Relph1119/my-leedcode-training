#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        index = 0
        for i in range(len(s)):
            if index < len(g) and g[index] <= s[i]:
                index += 1

        return index
# @lc code=end

