# Given a binary array, find the maximum number of consecutive 1s in this array.
#
# Example 1:
#
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
#
# Note:
#
#     The input array will only contain 0 and 1.
#     The length of input array is a positive integer and will not exceed 10,000


# 一种解决方案
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        res = []
        for i in nums:
            if i == 1:
                count += 1
                res.append(count)
            if i == 0:
                count = 0
        if sum(nums) == 0:
            return 0
        else:
            return max(res)

