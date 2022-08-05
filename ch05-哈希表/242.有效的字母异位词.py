#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        
        for x in s:
            s_dict[x] += 1

        for x in t:
            t_dict[x] += 1

        return s_dict == t_dict
# @lc code=end

