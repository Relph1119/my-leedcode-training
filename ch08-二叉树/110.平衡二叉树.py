#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_depth(node: TreeNode):
            if node is None:
                return 0

            left_depth = get_depth(node.left)
            if left_depth == -1:
                return -1

            right_depth = get_depth(node.right)
            if right_depth == -1:
                return -1
            
            if abs(left_depth - right_depth) > 1:
                return -1
            else:
                return  1 + max(left_depth, right_depth)
        
        return False if get_depth(root) == -1 else True
# @lc code=end

