#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traversal(root):
            if not root:
                return
            traversal(root.left)
            vec.append(root.val)
            traversal(root.right)
        
        vec = []
        traversal(root)
        for i in range(1, len(vec)):
            if vec[i] <= vec[i - 1]:
                return False
        return True
# @lc code=end

