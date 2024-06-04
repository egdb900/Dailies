class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = set(s)
        res = 0
        odd = 0
        for letter in letters:
            occurences = s.count(letter)
            if occurences % 2 == 0:
                res += occurences
            else:
                odd = 1
                res += occurences - 1
        res += odd
            
        return res
        


        