# Given an integer, write a function to determine if it is a power of two.


# 一种解决方案
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & n - 1)


# 另外一种解决方案
class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n % 2 == 0:
            n = n / 2
        return True if n == 1 else False

