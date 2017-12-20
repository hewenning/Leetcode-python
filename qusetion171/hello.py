# Related to question Excel Sheet Column Title
#
# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.


# 一种解决方案
from functools import reduce


class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return reduce(lambda x, y: x * 26 + y, map(lambda x: ord(x) - ord('A') + 1, s))


#　另外一种解决方案
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        col = 0
        for letter in s:
            col = col * 26 + ord(letter) - 64
        return col
