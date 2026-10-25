# No.34 Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.



# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        res = [-1] * 2

        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i+j)//2
            num = nums[m]
            if target > num:
                i = m + 1
            elif target < num:
                j = m - 1
            else:
                res[0] = m
                j = m - 1

        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i+j)//2
            num = nums[m]
            if target > num:
                i = m + 1
            elif target < num:
                j = m - 1
            else:
                res[1] = m
                i = m + 1

        return res

