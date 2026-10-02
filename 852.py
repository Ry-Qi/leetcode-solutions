# No.852 Peak Index in a Mountain Array

# You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

# Return the index of the peak element.

# Your task is to solve it in O(log(n)) time complexity.

# Example 1:

# Input: arr = [0,1,0]

# Output: 1

# Example 2:

# Input: arr = [0,2,1,0]

# Output: 1

# Example 3:

# Input: arr = [0,10,5,2]

# Output: 1

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        l, r = 0, len(arr)-1
        res = 0
        while l <= r:
            if l==r==len(arr)-1:
                res = l
                break
            i = (l+r)//2
            if arr[i+1] > arr[i]:
                l = i + 1
            elif arr[i+1] < arr[i]:
                res = i
                r = i - 1
        return res


print(Solution().peakIndexInMountainArray([1,2,3,4,5]))
