# # No.167 Two Sum 2
# You are given a 1-indexed array of integers numbers that is already sorted in non-decreasing order.

# Find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and
# numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers index1 and index2
# as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution.
# You may not use the same element twice.

# Your solution must use only constant extra space.

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].


class Solution:
    def twoSum1(self, numbers: list, target: int) -> list:

        # start with extreme values
        l, r = 0, len(numbers)-1

        while l<r:
            s = numbers[l] + numbers[r]
            if s < target:
                # nums[l] + nums[l+1, ..., r] < target
                l += 1
            elif s > target:
                # nums[l, ..., r-1] + nums[r] > target
                r -= 1
            else:
                return [l+1, r+1]

        return [-1, -1]

    def twoSum2(self, numbers: list, target: int) -> list:

        def TS(i, j):
            if i==j:
                return [-1, -1]
            nonlocal numbers
            s = numbers[i] + numbers[j]
            if s > target:
                return TS(i, j-1)
            if s < target:
                return TS(i+1, j)

            return [i+1, j+1]

        return TS(0, len(numbers)-1)

numbers = [2,7,11,15]

print(Solution().twoSum2(numbers, 9))