#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def traversal(root):
            if not root:
                return 
            traversal(root.left)
            vec.append(root.val)
            traversal(root.right)

        vec = []
        rec = float('inf')
        traversal(root)
        for i in range(1, len(vec)):
            rec = min(rec, abs(vec[i] - vec[i - 1]))
        return rec
# @lc code=end

