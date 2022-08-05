#
# @lc app=leetcode.cn id=669 lang=python3
#
# [669] 修剪二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val < low:
            right = self.trimBST(root.right, low, high)
            return right
        
        if root.val > high:
            left = self.trimBST(root.left, low, high)
            return left
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
# @lc code=end

