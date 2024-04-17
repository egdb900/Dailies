class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = ["a", "e", "i", "o", "u"]

        
        curr_vowels = 0
        substring = s[0:k]
        for i in range(k):
            if s[i] in vowels:
                curr_vowels += 1
        max_vowels = curr_vowels

        for i in range(len(s)-k):
            if s[i] in vowels:
                curr_vowels -= 1
            if s[i+k] in vowels:
                curr_vowels += 1
            if max_vowels < curr_vowels:
                max_vowels = curr_vowels
        
        return max_vowels


        