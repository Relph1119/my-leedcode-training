#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        

        def traversal(cur: TreeNode, count: int):
            if not cur.left and not cur.right:
                if count == 0:
                    result.append(path.copy())
                return 
            
            if cur.left:
                path.append(cur.left.val)
                traversal(cur.left, count - cur.left.val)
                path.pop()
            
            if cur.right:
                path.append(cur.right.val)
                traversal(cur.right, count - cur.right.val)
                path.pop()

            return

        result = []
        path = []

        if root is None:
            return result
        path.append(root.val)
        traversal(root, targetSum - root.val)
        return result

# @lc code=end

