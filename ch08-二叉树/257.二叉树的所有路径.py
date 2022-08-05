#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def traversal(cur: TreeNode, path, result):
            path.append(cur.val)

            if cur.left is None and cur.right is None:
                s_path = ""
                for i in range(len(path) - 1):
                    s_path += str(path[i])
                    s_path += "->"
            
                s_path += str(path[-1])
                result.append(s_path)

            if cur.left:
                traversal(cur.left, path, result)
                path.pop()
            if cur.right:
                traversal(cur.right, path, result)
                path.pop()

        result = []
        path = []
        if root is None:
            return result

        traversal(root, path, result)
        return result
            
# @lc code=end

