# 给定一组不同的整数 nums，返回所有可能的子集（幂集）。
#
# 注意事项：该解决方案集不能包含重复的子集。
#
# 例如，如果 nums = [1,2,3]，结果为以下答案：
#
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


# 一種解決方案
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)
