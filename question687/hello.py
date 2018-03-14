# Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.
#
# Note: The length of path between two nodes is represented by the number of edges between them.
#
# Example 1:
#
# Input:
#
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output:
#
# 2
# Example 2:
#
# Input:
#
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output:
#
# 2
# Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.


# 一种解决方案
# The approach is similar to the Diameter of Binary Tree question except that we reset the left/right to 0 whenever the current node does not match the children node value.
#
# In the Diameter of Binary Tree question, the path can either go through the root or it doesn’t.
#
# Imgur
#
# Hence at the end of each recursive loop, return the longest length using that node as the root so that the node’s parent can potentially use it in its longest path computation.
#
# We also use an external variable longest that keeps track of the longest path seen so far.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        longest = [0]

        def traverse(node):
            if not node:
                return 0
            left_len, right_len = traverse(node.left), traverse(node.right)
            left = (left_len + 1) if node.left and node.left.val == node.val else 0
            right = (right_len + 1) if node.right and node.right.val == node.val else 0
            longest[0] = max(longest[0], left + right)
            return max(left, right)

        traverse(root)
        return longest[0]
