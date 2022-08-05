#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traversal(cur: TreeNode, count: int) -> bool:
            if not cur.left and not cur.right and count == 0:
                return True
            if not cur.left and not cur.right:
                return False
            
            if cur.left:
                if traversal(cur.left, count - cur.left.val):
                    return True
            if cur.right:
                if traversal(cur.right, count - cur.right.val):
                    return True
            
            return False
        
        if root is None:
            return False
        
        return traversal(root, targetSum - root.val)
# @lc code=end

