#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self._head = Node(0)
        self._size = 0        

    def get(self, index: int) -> int:
        if 0 <= index < self._size:
            node = self._head
            for _ in range(index + 1):
                node = node.next
            return node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self._size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        elif index > self._size:
            return 
        
        self._size += 1
        new_node = Node(val)
        prev_node, cur_node = None, self._head
        for _ in range(index + 1):
            prev_node, cur_node = cur_node, cur_node.next
        else:
            prev_node.next, new_node.next = new_node, cur_node

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self._size:
            self._size -= 1
            prev_node, cur_node = None, self._head
            for _ in range(index + 1):
                prev_node, cur_node = cur_node, cur_node.next
            else:
                prev_node.next, cur_node.next = cur_node.next, None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

