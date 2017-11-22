# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


# 一种解决方案
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(list(set(nums))) * 2 - sum(nums)


# 另一种解决方案
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(operator.xor, nums)
    
    def singleNumber1(self, nums):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for key, val in dic.items():
            if val == 1:
                return key

    def singleNumber2(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res

    def singleNumber3(self, nums):
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber4(self, nums):
        return reduce(lambda x, y: x ^ y, nums)
