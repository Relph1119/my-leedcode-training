#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def traversal(inorder, postorder):
            if not postorder:
                return None
            
            # 后序的最后一个节点为根节点
            root_value = postorder[-1]
            root = TreeNode(root_value)

            # 查找切割点
            delimiter_index = inorder.index(root_value)
            
            # 切割中序数组
            left_inorder = inorder[:delimiter_index]
            right_inorder = inorder[delimiter_index + 1:]
            
            # 切割后序数组
            left_postorder = postorder[:len(left_inorder)]
            right_postorder = postorder[len(left_inorder): len(postorder) - 1]

            root.left = traversal(left_inorder, left_postorder)
            root.right = traversal(right_inorder, right_postorder)

            return root
        
        return traversal(inorder, postorder)
# @lc code=end

