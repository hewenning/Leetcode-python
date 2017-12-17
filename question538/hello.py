# Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
#
# Example:
#
# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13
#
# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13


# 一种解决方案
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def visit1(root):
            if root:
                visit1(root.left)
                vals.append(root.val)
                visit1(root.right)

        vals = []
        visit1(root)

        self.s = 0

        def visit2(root):
            if root:
                visit2(root.right)
                self.s += vals.pop()
                root.val = self.s
                visit2(root.left)

        visit2(root)

        return root