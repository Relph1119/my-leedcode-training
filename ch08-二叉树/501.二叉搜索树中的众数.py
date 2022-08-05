#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = TreeNode()
        self.count = 0
        self.max_count = 0
        self.result = []

    def search_BST(self, cur: TreeNode):
        if not cur:
            return None
        
        # 遍历左边
        self.search_BST(cur.left)

        # 遍历中间
        if not self.pre:
            self.count = 1
        elif self.pre.val == cur.val:
            self.count + 1
        else:
            self.count = 1
        
        self.pre = cur

        if self.count == self.max_count:
            self.result.append(cur.val)
        
        if self.count > self.max_count:
            self.max_count = self.count
            # 清空result
            self.result = [cur.val]

        # 遍历右边
        self.search_BST(cur.right)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        self.search_BST(root)
        return self.result
# @lc code=end

