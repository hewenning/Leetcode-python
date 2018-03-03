# Given an integer, write a function to determine if it is a power of three.
#
# Follow up:
# Could you do it without using any loop / recursion?
#
# Credits:
# Special thanks to @dietpepsi for adding this problem and creating all test cases.


# 一种解决方案
class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False

        while n % 3 == 0:
            n = n / 3

        return True if n == 1 else False


# 更好的解决方案
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 1162261467 % n == 0
