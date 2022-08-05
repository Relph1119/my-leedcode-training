#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if root is None:
            return result

        from collections import deque
        que = deque([root])
        while que:
            size = len(que)
            vec = []
            for _ in range(size):
                node = que.popleft()
                vec.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            result.append(vec)

        return result
# @lc code=end

