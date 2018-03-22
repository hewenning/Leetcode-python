# Rotate an array of n elements to the right by k steps.
#
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
#
# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
#
# [show hint]
#
# Related problem: Reverse Words in a String II


# 一种解决方案
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]


# 另外一种解决方案
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n, k, j = len(nums), k % len(nums), 0
        while n > 0 and k % n != 0:
            for i in range(0, k):
                nums[j + i], nums[len(nums) - k + i] = nums[len(nums) - k + i], nums[j + i] # swap
            n, j = n - k, j + k
            k = k % n


# 其他的解决方案
Classical
3 - step
array
rotation:
reverse
the
first
n - k
elements

reverse
the
rest
of
them

reverse
the
entire
array


class Solution(object):
    def rotate(self, nums, k):
        if k is None or k <= 0:
            return
        k, end = k % len(nums), len(nums) - 1
        self.reverse(nums, 0, end - k)
        self.reverse(nums, end - k + 1, end)
        self.reverse(nums, 0, end)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1


O(n) in time, O(1) in space

Rotate
k
times:
Each
rotation, we
move
the
n - 1
to
the
back
of
the
array
one
by
one and we
do
rotation
k
times.


class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        for i in xrange(0, k):
            tmp = nums[-1]
            for j in xrange(0, len(nums) - 1):
                nums[len(nums) - 1 - j] = nums[len(nums) - 2 - j]
            nums[0] = tmp


O(n ^ 2) in time, O(1) in space

It
can’t
pass
the
OJ
due
to
TLE.

Recursive
solution
put
the
shorter
part in the
correct
position
then
do
the
rest
of
them
iteratively.This is not necessarily
to
be
a
recursive
solution.


class Solution(object):
    def rotate(self, nums, k):
        self.helper(0, len(nums) - 1 - (k % len(nums)), len(nums) - 1, nums)  # mid belongs to left part

    def helper(self, start, mid, end, nums):
        left, right = mid - start, end - mid - 1
        if left < 0 or right < 0:
            return
        if left > right:
            for j in xrange(mid + 1, end + 1):
                nums[j], nums[start] = nums[start], nums[j]
                start += 1
            self.helper(start, mid, end, nums)
        elif right >= left:
            i = mid
            while i >= start:
                nums[i], nums[end] = nums[end], nums[i]
                i, end = i - 1, end - 1
            if left != right:
                self.helper(start, mid, end, nums)


O(n) in time, O(n) in space

Iterative and improved
solution:
put
the
last
k
elements in correct
position(ahead) and do
the
remaining
n - k.Once
finish
swap, the
n and k
decrease.


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n, k, j = len(nums), k % len(nums), 0
        while n > 0 and k % n != 0:
            for i in xrange(0, k):
                nums[j + i], nums[len(nums) - k + i] = nums[len(nums) - k + i], nums[j + i]  # swap
            n, j = n - k, j + k
            k = k % n


O(n) in time, O(1) in space