class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        c = 0
        for token in t:
            if c < len(s) and token == s[c]:
                c += 1
        return c == len(s)
        
        