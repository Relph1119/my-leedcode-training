#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 颠倒字符串中的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s): 
        return ' '.join(s.split()[::-1])

# @lc code=end
