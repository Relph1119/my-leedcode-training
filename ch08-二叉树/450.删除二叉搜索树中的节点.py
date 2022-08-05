#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if root.val == key:
            if not root.left and not root.right:
                del root
                return None
            elif not root.left and root.right:
                tmp = root
                root = root.right
                del tmp
                return root
            elif not root.right and root.left:
                tmp = root
                root = root.left
                del tmp
                return root
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                tmp = root
                root = root.right
                del tmp
                return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)

        return root     
# @lc code=end

