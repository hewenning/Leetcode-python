# 给定一个二叉树，返回其中序遍历。
#
# 例如：
# 给定二叉树 [1,null,2,3],
#
#    1
#     \
#      2
#     /
#    3
# 返回 [1,3,2].
#
# 说明: 递归算法很简单，你可以通过迭代算法完成吗？


# 一种解决方案
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)

    # iteratively
    def inorderTraversal(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
