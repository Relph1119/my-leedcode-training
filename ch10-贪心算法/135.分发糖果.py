#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy_vec = [1] * len(ratings)

        # 从前向后遍历
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candy_vec[i] = candy_vec[i - 1] + 1


        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy_vec[i] = max(candy_vec[i], candy_vec[i + 1] + 1)
        
        return sum(candy_vec)
# @lc code=end

