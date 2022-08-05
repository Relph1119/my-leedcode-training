#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution:
    def is_valid(self, s, start, end):
        if start > end:
            return False
        
        if s[start] == '0' and start != end:
            return False
        
        if not (0 <= int(s[start:end+1]) <= 255):
            return False
        
        return True

    def restoreIpAddresses(self, s: str) -> List[str]:

        def backtracking(s, start_index, point_num):
            if point_num == 3:
                if self.is_valid(s, start_index, len(s) - 1):
                    result.append(s[:])
                return
            
            for i in range(start_index, len(s)):
                if self.is_valid(s, start_index, i):
                    s = s[:i+1] + '.' + s[i+1:]
                    point_num += 1
                    backtracking(s, i + 2, point_num)
                    point_num -= 1
                    s = s[:i+1] + s[i+2:]
                else:
                    break
                            
        result = []
        if len(s) > 12:
            return []
        backtracking(s, 0, 0)
        return result
# @lc code=end

