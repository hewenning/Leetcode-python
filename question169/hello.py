# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.


# 一种解决方案
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return [x for x in set(nums) if nums.count(x) >= len(nums) / 2][0]


# 另外一种解决方案
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=0
        nums.sort()
        return nums[len(nums)//2]
