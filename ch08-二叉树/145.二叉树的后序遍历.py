#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def traversal(root: TreeNode):
            if root is None:
                return result

            traversal(root.left)
            traversal(root.right)
            result.append(root.val)

        traversal(root)

        return result
# @lc code=end

