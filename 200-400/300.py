
# No.300 Longest Increasing subsequence
# Given an integer array nums, return the length of the longest strictly increasing subsequence.



# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: nums = [0,1,0,3,2,3]
# Output: 4


class Solution:
    def lengthOfLIS(self, nums) -> int:
        cache = {}
        def lis(end):
            if end==0:
                return 1
            if end in cache:
                return cache[end]

            res = 1
            for s in range(0, end):
                if nums[end]>nums[s]:
                    sub = lis(s)
                    res = max(res, sub+1)
            cache[end] = res
            return res
        res = 0
        for i in range(len(nums)):
            res = max(res, lis(i))
        return res



print(Solution1().lengthOfLIS([10,9,2,5,3,7,101,18]))


