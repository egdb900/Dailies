class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        tokens = s.split(" ")
        tokens = filter(lambda x: x != "", tokens)

        tokens = tokens[::-1]
        res = " ".join(tokens)
        
        return res