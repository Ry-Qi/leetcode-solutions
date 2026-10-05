# No.20 Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true


class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if not st:
                st.append(c)
            else:
                if c in ['(', '{', '[']: st.append(c)
                else:
                    if (c==')' and st[-1]!='(' or
                        c=='}' and st[-1]!='{' or
                        c==']' and st[-1]!='['):
                        return False
                    st.pop()

        return not st