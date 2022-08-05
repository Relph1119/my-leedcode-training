#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.s = ''
        self.result = []
        self.letter_map = {
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz"
        }

    def backtracking(self, digits, index):
        if index == len(digits):
            self.result.append(self.s)
            return
        
        letters = self.letter_map[digits[index]]
        for i in range(len(letters)):
            self.s += letters[i]
            self.backtracking(digits, index + 1)
            self.s = self.s[:-1]

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        self.backtracking(digits, 0)
        return self.result
# @lc code=end

