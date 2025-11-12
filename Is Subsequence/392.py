class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if len(s) > len(t):
            return False

        curr = 0
        for i in range(len(t)):
            if s[curr] == t[i]:
                curr += 1
                if curr == len(s): 
                    return True
        return False
            