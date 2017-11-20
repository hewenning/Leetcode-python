# Write a function that takes a string as input and returns the string reversed.
#
# Example:
# Given s = "hello", return "olleh".


# 一个解决方案
class Solution:
    def reverseString(s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


s="hello"
print(Solution.reverseString(s))