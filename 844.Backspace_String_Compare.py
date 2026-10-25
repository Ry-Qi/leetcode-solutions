# No. 844 BackSpace String Compare
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.



# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st = []
        for c in s:
            if c=='#' and st:
                st.pop()
            elif c!='#':
                st.append(c)
        s = ''.join(st)
        st = []
        for c in t:
            if c=='#' and st:
                st.pop()
            elif c!='#':
                st.append(c)
        t = ''.join(st)
        return s == t
