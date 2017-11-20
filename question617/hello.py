#  Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
#
# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
#
# Example 1:
#
# Input:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7
# Output:
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7
#
# Note: The merging process must start from the root nodes of both trees.


# # 一个解决方案
# Let's create a recursive solution.
#
#     If both trees are empty then we return empty.
#     Otherwise, we will return a tree. The root value will be t1.val + t2.val, except these values are 0 if the tree is empty.
#     The left child will be the merge of t1.left and t2.left, except these trees are empty if the parent is empty.
#     The right child is similar.
#
# def mergeTrees(self, t1, t2):
#     if not t1 and not t2: return None
#     ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
#     ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
#     ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
#     return ans

# 一个解决方案
def mergeTrees(self, t1, t2):
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """
    if not t1 and not t2:
        return

    if not t1:
        res = t2
    elif not t2:
        res = t1
    else:
        res = TreeNode(t1.val + t2.val)
        res.left = self.mergeTrees(t1.left, t2.left)
        res.right = self.mergeTrees(t1.right, t2.right)

    return res