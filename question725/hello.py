# Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".
#
# The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.
#
# The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.
#
# Return a List of ListNode's representing the linked list parts that are formed.
#
# Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
# Example 1:
# Input:
# root = [1, 2, 3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The input and each element of the output are ListNodes, not arrays.
# For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but it's string representation as a ListNode is [].
# Example 2:
# Input:
# root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
# Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
# Explanation:
# The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
# Note:
#
# The length of root will be in the range [0, 1000].
# Each value of a node in the input will be an integer in the range [0, 999].
# k will be an integer in the range [1, 50].


# 一種解決方案
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        # find length of the linked list using slow and fast pointer algorithm
        slow = fast = root
        length = 1  # index of slow pointer node, 1-based
        while True:
            if not fast:
                length = (length - 1) * 2  # even length list
                break
            elif not fast.next:
                length = length * 2 - 1  # odd length list
                break
            length += 1
            slow = slow.next
            fast = fast.next.next
        n = length // k  # number of nodes in each linked list in array
        r = length % k  # number of remaining nodes to split among linked lists

        # split linked list into smaller lists and put them into array
        result = [ListNode("") for i in range(k)]  # initialize an array of dummy nodes
        i = 0  # index of current linked list in array
        curr = root
        while curr:
            dummy = result[i]  # current dummy node
            for j in range(n):
                dummy.next = curr
                dummy = dummy.next
                curr = curr.next
            if r:  # while we still have remaining nodes
                r -= 1
                dummy.next = curr
                curr = curr.next
                dummy = dummy.next
            dummy.next = None  # detach current linked list from original list
            result[i] = result[i].next  # move pointer to the 1st node
            i += 1
        return result
