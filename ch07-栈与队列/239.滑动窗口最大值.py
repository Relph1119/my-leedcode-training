#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class MyQueue:
    def __init__(self):
        self.queue = []

    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.pop(0)

    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    def front(self):
        return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = MyQueue()
        result = []
        for i in range(k):
            que.push(nums[i])
        result.append(que.front())

        for i in range(k, len(nums)):
            que.pop(nums[i - k])
            que.push(nums[i])
            result.append(que.front())
        
        return result

# @lc code=end

