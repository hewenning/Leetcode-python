# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
#
# Input: 16
# Returns: True
# Example 2:
#
# Input: 14
# Returns: False


# 一种解决方案
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 0
        while 1:
            if num == i * i:
                return True
            i = i + 1
            if num < i * i:
                return False
