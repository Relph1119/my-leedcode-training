#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_sum = 0
        total_sum = 0
        start = 0
        for i in range(len(gas)):
            cur_sum += gas[i] - cost[i]
            total_sum += gas[i] - cost[i]
            if cur_sum < 0:
                start = i + 1
                cur_sum = 0
        
        if total_sum < 0:
            return -1
        
        return start
# @lc code=end

