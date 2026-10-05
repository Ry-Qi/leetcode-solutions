# No.35 Search Insert Positon
# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.



# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        i, j = 0, len(nums)-1

        while i <= j:
            m = (i+j)//2
            n = nums[m]
            if target > n:
                i = m + 1
            elif target < n:
                j = m - 1
            else:
                return m
        # [1, 3, 5, 7]
        return i
