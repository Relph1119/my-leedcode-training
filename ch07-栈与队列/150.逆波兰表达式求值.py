#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(token)
            else:
                num1, num2 = stack.pop(), stack.pop()
                val = int(eval(f'{num2} {token} {num1}'))
                stack.append(val)
        
        return int(stack.pop())
# @lc code=end

