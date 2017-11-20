# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
# Example 1:
#
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
#
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.


# 一个解决方案
class Solution:
    def reverseWords(s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])[::-1]


s = "Let's take LeetCode contest"
a = Solution.reverseWords(s)
print(a)