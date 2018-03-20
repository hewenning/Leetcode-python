# Implement int sqrt(int x).
#
# Compute and return the square root of x.
#
# x is guaranteed to be a non-negative integer.
#
#
# Example 1:
#
# Input: 4
# Output: 2
# Example 2:
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.


# 一种解决方案
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l <= r:
            mid = (r+l)/2
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid
            elif mid*mid > x:
                r = mid - 1
            else:
                l = mid + 1
