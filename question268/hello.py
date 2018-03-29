# 给出一个包含
# 0, 1, 2, ..., n
# 中
# n
# 个数的序列，找出
# 0..n
# 中没有出现在序列中的那个数。
#
# 案例
# 1
#
# 输入: [3, 0, 1]
# 输出: 2
#
# 案例
# 2
#
# 输入: [9, 6, 4, 2, 3, 5, 7, 0, 1]
# 输出: 8
#
# 注意事项:
# 您的算法应该以线性复杂度运行。你能否仅使用恒定的额外空间复杂度来实现它？


# 一種解決方案
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        sum_value = 0
        while i != n:
            sum_value -= nums[i]
            sum_value += i
            i += 1
        return sum_value + n


# 另外一種解決方案
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        sum_value = 0
        while i != n:
            sum_value += nums[i]
            i += 1
        return int(n * (n + 1) / 2 - sum_value)
