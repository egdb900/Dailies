class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        c = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            if c[l] in vowels and c[r] in vowels:
                c[l], c[r] = c[r], c[l]
                l += 1
                r -= 1
            elif s[l] not in vowels:
                l += 1
            elif s[r] not in vowels:
                r -= 1
            else:
                l += 1
                r -= 1
        return ''.join(c)
            