# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
# Given s = "hello", return "holle".
#
# Example 2:
# Given s = "leetcode", return "leotcede".
#
# Note:
# The vowels does not include the letter "y".


# 一种解决方案
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)


# 另外一种解决方案
def reverseVowels(self, s):
    vowels = (c for c in reversed(s) if c in 'aeiouAEIOU')
    return re.sub('(?i)[aeiou]', lambda m: next(vowels), s)