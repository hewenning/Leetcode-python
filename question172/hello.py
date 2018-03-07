# Given an integer n, return the number of trailing zeroes in n!.
#
# Note: Your solution should be in logarithmic time complexity.


# 一种解决方案
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 4:
            return 0
        else:
            return int(n / 5 + self.trailingZeroes(n / 5))
