# 给定一个含有不同数字的集合，返回所有可能的全排列。
#
# 比如，
# [1,2,3] 具有如下排列：
#
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


# 一種解決方案
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
