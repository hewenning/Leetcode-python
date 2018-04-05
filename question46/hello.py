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
        return [[n] + p
            for i, n in enumerate(nums)
            for p in self.permute(nums[:i] + nums[i+1:])] or [[]]


# 其他的解決方案
# Solution 1: Recursive, take any number as first
#
# Take any number as the first number and append any permutation of the other numbers.
#
# def permute(self, nums):
#     return [[n] + p
#             for i, n in enumerate(nums)
#             for p in self.permute(nums[:i] + nums[i+1:])] or [[]]
# Solution 2: Recursive, insert first number anywhere
#
# Insert the first number anywhere in any permutation of the remaining numbers.
#
# def permute(self, nums):
#     return nums and [p[:i] + [nums[0]] + p[i:]
#                      for p in self.permute(nums[1:])
#                      for i in range(len(nums))] or [[]]
# Solution 3: Reduce, insert next number anywhere
#
# Use reduce to insert the next number anywhere in the already built permutations.
#
# def permute(self, nums):
#     return reduce(lambda P, n: [p[:i] + [n] + p[i:]
#                                 for p in P for i in range(len(p)+1)],
#                   nums, [[]])
# Solution 4: Using the library
#
# def permute(self, nums):
#     return list(itertools.permutations(nums))
# That returns a list of tuples, but the OJ accepts it anyway. If needed, I could easily turn it into a list of lists:
#
# def permute(self, nums):
#     return map(list, itertools.permutations(nums))
