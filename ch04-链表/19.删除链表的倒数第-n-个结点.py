#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy_head = ListNode()
        dummy_head.next = head

        slow, fast = dummy_head, dummy_head
        while n != 0:
            fast = fast.next
            n -= 1

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        
        return dummy_head.next
# @lc code=end

