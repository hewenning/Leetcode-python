# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
# Example 1:
# Input: "abab"
#
# Output: True
#
# Explanation: It's the substring "ab" twice.
# Example 2:
# Input: "aba"
#
# Output: False
# Example 3:
# Input: "abcabcabcabc"
#
# Output: True
#
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)


# 一种解决方案
class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        index = 1
        substring = str(s[0])
        while(index < len(s)):
            if substring == s[index:index+len(substring)]:
                index += len(substring)
            else:
                index = len(substring)+1
                substring = s[:len(substring)+1]
                if(index >= len(s)):
                    return False
        return len(substring) != len(s)
