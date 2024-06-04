class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = set(s)
        res = len(s)
        odd = 0
        for letter in letters:
            occurences = s.count(letter)
            if occurences % 2 != 0:
                odd += 1
        if odd > 0:
            res = res - odd + 1
            
        return res
        


        