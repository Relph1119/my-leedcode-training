#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from unittest import result


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        depth = 0

        from collections import deque

        que = deque([root])
        while que:
            size = len(que)
            depth += 1
            for _ in range(size):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                if node.left is None and node.right is None:
                    return depth
        
        return depth
# @lc code=end

