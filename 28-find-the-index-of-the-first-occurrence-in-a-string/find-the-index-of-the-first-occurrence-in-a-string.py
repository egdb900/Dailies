class Solution(object):
    def strStr(self, haystack, needle):
        x = 0
        while x <= len(haystack) - len(needle):
            if haystack[x:x + len(needle)] == needle:
                return x
            x += 1
        return -1
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        