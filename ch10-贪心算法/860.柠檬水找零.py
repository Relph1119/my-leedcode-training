#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten, twenty = 0, 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
            if bill == 10:
                if five <= 0:
                    return False
                five -= 1
                ten += 1
            if bill == 20:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                    twenty += 1
                elif five >= 3:
                    five -= 3
                    twenty += 1
                else:
                    return False
        
        return True
# @lc code=end

