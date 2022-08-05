#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []

        if len(intervals) == 0:
            return result

        intervals = sorted(intervals, key=lambda x: x[0])
        
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
        
        return result
# @lc code=end

