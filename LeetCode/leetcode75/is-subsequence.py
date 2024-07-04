class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        i = 0
        while i < len(t) and s_pointer < len(s):
            if s[s_pointer] == t[i]:
                s_pointer += 1
            i += 1
        return s_pointer == len(s)
