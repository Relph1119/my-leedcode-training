#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = dict()
        for i in range(len(nums)):
            count_map[nums[i]] = count_map.get(nums[i], 0) + 1

        pri_que = []
        for key, freq in count_map.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k:
                heapq.heappop(pri_que)

        result = [0] * k
        for i in range(k-1, -1, -1):
            # print key
            result[i] = heapq.heappop(pri_que)[1]
        
        return result
# @lc code=end

