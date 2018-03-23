# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output:  321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


# 一种解决方案
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = (x > 0) - (x < 0)
        r = int(str(x*s)[::-1])
        return s*r * (r < 2**31)
