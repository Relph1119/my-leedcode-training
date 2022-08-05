#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        records = dict()
        for a in nums1:
            for b in nums2:
                records[a+b] = records.get(a+b, 0) + 1

        count = 0 
        for c in nums3:
            for d in nums4:
                key = - c - d
                if key in records:
                    count += records[key]
        
        return count
# @lc code=end

