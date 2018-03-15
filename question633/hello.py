#
# Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.
#
# Example 1:
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
# Example 2:
# Input: 3
# Output: False


# 一种解决方案
class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        maxs = 1
        while (maxs * maxs) < c:
            maxs += 1

        lo = 0
        hi = maxs
        while lo <= hi:
            if ((lo * lo) + (hi * hi)) == c:
                return True
            if ((lo * lo) + (hi * hi)) < c:
                lo += 1
            if ((lo * lo) + (hi * hi)) > c:
                hi -= 1

        # Bruthe force until maxs O(n^2)
        # for i in range(1,maxs):
        #    for j in range(1,maxs):
        #        if c == (i*i + j*j):
        #            return True

        return False
