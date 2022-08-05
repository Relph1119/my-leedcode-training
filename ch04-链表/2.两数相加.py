#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 虚拟头节点
        dummy_head = ListNode()
        p = dummy_head
        # 进位
        carry = 0
        # 两个链表指针
        p1, p2 = l1, l2
        while p1 or p2 or carry > 0:
            val = carry
            if p1:
                val += p1.val
                p1 = p1.next
            if p2:
                val += p2.val
                p2 = p2.next
            
            carry = val // 10
            val = val % 10

            p.next = ListNode(val)
            p = p.next
        
        return dummy_head.next

# @lc code=end

