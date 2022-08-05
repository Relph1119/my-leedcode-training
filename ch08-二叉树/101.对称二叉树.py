#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def compare(left: TreeNode, right: TreeNode) -> bool:
            if left is None and right is not None:
                return False
            elif left is not None and right is None:
                return False
            elif left is None and right is None:
                return True
            elif left.val != right.val:
                return False
            
            outside = compare(left.left, right.right)
            inside = compare(left.right, right.left)
            return outside and inside
        
        if root is None:
            return True
        return compare(root.left, root.right)
# @lc code=end

