# No.22 Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of
# well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

class Solution:
    def generateParenthesis(self, n) -> list:

        left, right = 0, 0
        res, path = [], []

        def dfs():
            nonlocal left, right, n, path

            if left==right==n:
                res.append(''.join(path))
                return

            if left < n:
                path.append('(')
                left += 1
                dfs()
                path.pop()
                left -= 1

            if right < n:
                if left > right:
                    path.append(')')
                    right += 1
                    dfs()
                    path.pop()
                    right -= 1

        dfs()
        return res

print(Solution().generateParenthesis(5))



