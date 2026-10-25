# No. 1963 Minimum Swaps to Make String Balanced
# You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

# A string is called balanced if and only if:

# It is the empty string, or
# It can be written as AB, where both A and B are balanced strings, or
# It can be written as [C], where C is a balanced string.
# You may swap the brackets at any two indices any number of times.

# Return the minimum number of swaps to make s balanced.


# Example 1:

# Input: s = "][]["
# Output: 1
# Explanation: You can make the string balanced by swapping index 0 with index 3.
# The resulting string is "[[]]".


# ']['             1
# ']][['           1
# ']]][[['         2
# '[][][[]]'       2

class Solution:
    def minSwaps(self, s: str) -> int:
        openings = []
        closing = []
        for i, c in enumerate(s):
            if c=='[':
                openings.append(i)
            elif c==']':
                if openings:
                    openings.pop()
                else:
                    closing.append(i)
        if len(openings) != len(closing):
            return -1
        return len(openings)//2 + len(openings)%2

    def minSwaps(self, s: str) -> int:
        openings = closings = 0
        for i, c in enumerate(s):
            if c=='[':
                openings += 1
            elif c==']':
                if openings:
                    openings -= 1
                else:
                    closings += 1

        return openings//2 + openings%2
