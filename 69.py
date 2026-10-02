# No.69 Sqrt()

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.


# Constraints:

# 0 <= x <= 231 - 1

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        #[0,1,2,3,4,5,6,7,8]
        while l <=r:
            i = (l+r)//2
            if x > i*i:
                l = i + 1
            elif x < i*i:
                r = i - 1
            else:
                return i
        # key
        return r

    def mySqrt2(self, x: int) -> int:
        l, r = 0, x
        #[0,1,2,3,4,5,6,7,8]
        res = -1
        while l <=r:
            i = (l+r)//2
            if x > i*i:
                l = i + 1
                res = i
            elif x < i*i:
                r = i - 1
            else:
                return i
        return res
