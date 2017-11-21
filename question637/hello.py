# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
#
# Example 1:
#
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
#
# Note:
#
#     The range of node's value is in the range of 32-bit signed integer.


# 一种解决方案
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        if not root: return res
        q = [root]
        while q:
            q1 = []
            total = 0
            cnt = 0
            while q:
                node = q.pop()
                if node.left: q1.append(node.left)
                if node.right: q1.append(node.right)
                total += node.val
                cnt += 1
            res.append(total * 1.0 / cnt)
            q = list(q1)
        return res



# 另一种解决方案
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        info = []
        def dfs(node, depth = 0):
            if node:
                if len(info) <= depth:
                    info.append([0, 0])
                info[depth][0] += node.val
                info[depth][1] += 1
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        dfs(root)

        return [s/float(c) for s, c in info]