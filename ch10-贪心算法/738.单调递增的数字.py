#
# @lc app=leetcode.cn id=738 lang=python3
#
# [738] 单调递增的数字
#

# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        str_num = list(str(n))
        for i in range(len(str_num) - 1, 0, -1):
            if int(str_num[i - 1]) > int(str_num[i]):
                str_num[i - 1] = str(int(str_num[i - 1]) - 1)
                str_num[i:] = '9' * (len(str_num) - i)
        
        return int("".join(str_num))
# @lc code=end

