#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.st_in = []
        self.st_out = []

    def push(self, x: int) -> None:
        self.st_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        
        if self.st_out:
            return self.st_out.pop()
        else:
            for i in range(len(self.st_in)):
                self.st_out.append(self.st_in.pop())
            return self.st_out.pop()

    def peek(self) -> int:
        res = self.pop()
        self.st_out.append(res)
        return res

    def empty(self) -> bool:
        return not (self.st_in or self.st_out)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

