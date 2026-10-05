# No.18 4 Sum

# Given an array nums of n integers,
# return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.


# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

class Solution:
    def fourSum(self, nums: list, target: int) -> list:
        nums.sort()
        sz, res = len(nums), []
        i,j = 0, 1
        while i < sz-3:
            if i>0 and nums[i]==nums[i-1]:
                i+=1
                continue
            j = i+1
            while j < sz-2:
                if j>i+1 and nums[j]==nums[j-1]:
                    j+=1
                    continue
                l, r = j+1, sz-1
                while l < r:
                    s = nums[i]+nums[l]+nums[r]+nums[j]
                    if s > target: r-=1
                    elif s < target: l+=1
                    else:
                        res.append([nums[i], nums[l], nums[r], nums[j]])
                        l+=1
                        while l<sz and nums[l]==nums[l-1]: l+=1
                j += 1
            i += 1
        return res


s = input().split()
n, target = int(s[0]), int(s[1])

nums = list(map(int, input().split()))

print(Solution().fourSum(nums, target))
