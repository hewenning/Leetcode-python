# Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
#
# Please note that the string does not contain any non-printable characters.
#
# Example:
#
# Input: "Hello, my name is John"
# Output: 5


# 一种解决方案
class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
