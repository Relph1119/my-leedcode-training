#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traversal(cur, p, q):
            if not cur:
                return cur
            
            # 遍历左边
            if cur.val > p.val and cur.val > q.val:
                left = traversal(cur.left, p, q)
                if left:
                    return left
            
            # 遍历右边
            if cur.val < p.val and cur.val < q.val:
                right = traversal(cur.right, p, q)
                if right:
                    return right
            
            return cur

        return traversal(root, p, q)
# @lc code=end

