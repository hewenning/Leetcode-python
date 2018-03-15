# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.


# 一种解决方案
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.isPalindrome(s, 0, len(s) - 1, 0)

    def isPalindrome(self, s, start, end, delCount):
        if delCount > 1:
            return False
        while start < end:
            if s[start] != s[end]:
                break
            start += 1
            end -= 1
        if (start == end) or (start == end + 1):
            return True
        return any(
            [self.isPalindrome(s, start + 1, end, delCount + 1), self.isPalindrome(s, start, end - 1, delCount + 1)])
