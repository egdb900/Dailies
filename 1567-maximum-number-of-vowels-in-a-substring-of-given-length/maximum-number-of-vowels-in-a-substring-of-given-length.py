class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = ["a", "e", "i", "o", "u"]

        
        curr_vowels = 0
        for token in s[:k]:
            if token in vowels:
                curr_vowels += 1
        max_vowels = curr_vowels

        for i in range(len(s)-k):
            if s[i] in vowels:
                curr_vowels -= 1
            if s[i+k] in vowels:
                curr_vowels += 1
            max_vowels = max(max_vowels, curr_vowels)
        return max_vowels


        