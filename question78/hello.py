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


# 另外一種解決方案
def subsets2(self, nums):
    res = []
    nums.sort()
    for i in range(1<<len(nums)):
        tmp = []
        for j in range(len(nums)):
            if i & 1 << j:  # if i >> j & 1:
                tmp.append(nums[j])
        res.append(tmp)
    return res


# 另外一種解決方案
def subsets(self, nums):
    res = [[]]
    for num in sorted(nums):
        res += [item+[num] for item in res]
    return res


# 一行的解決方案
def subsets(self, nums):
    return reduce(lambda L, ele: L + [l + [ele] for l in L], nums, [[]])

def subsets(self, nums):
    [[x for x in l if x is not None] for l in itertools.product(*zip(nums, [None] * len(nums)))]

def subsets(self, nums):
    [l for n in range(len(nums) + 1) for l in itertools.combinations(nums, n)]
