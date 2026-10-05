# No. 76
# Given two strings s and t of lengths m and n respectively,
# return the minimum window substring of s such that
# every character in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        total = len(count_t)

        l, r = 0, 0
        left, right, valid = 0, float('inf'), 0
        window_count = Counter()
        # [l, r)
        while r < len(s) or valid==total:
            if valid < total:
                window_count[s[r]]+=1
                if window_count[s[r]] == count_t[s[r]]: valid+=1
                r+=1
            else: #[l, r)
                if r-l < right-left: right, left = r, l
                window_count[s[l]]-=1
                if window_count[s[l]] == count_t[s[l]]-1: valid-=1
                l+=1
        if right == float('inf'): return ""

        return s[left: right]

print(Solution().minWindow("ADOBECODEBANC", "ABC"))



