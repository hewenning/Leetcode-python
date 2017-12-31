# Given two strings s and t, write a function to determine if t is an anagram of s.
#
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?


# 一种解决方案
def isAnagram1(self, s, t):
    dic1, dic2 = {}, {}
    for item in s:
        dic1[item] = dic1.get(item, 0) + 1
    for item in t:
        dic2[item] = dic2.get(item, 0) + 1
    return dic1 == dic2


def isAnagram2(self, s, t):
    dic1, dic2 = [0] * 26, [0] * 26
    for item in s:
        dic1[ord(item) - ord('a')] += 1
    for item in t:
        dic2[ord(item) - ord('a')] += 1
    return dic1 == dic2


def isAnagram3(self, s, t):
    return sorted(s) == sorted(t)


# 另外一种解决方案
def isAnagram1(self, s, t):
    return collections.Counter(s) == collections.Counter(t)


# 一种解决方案


def isAnagram(self, s, t):
        return all([s.count(c)==t.count(c) for c in string.ascii_lowercase])
