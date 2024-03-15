class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        def divisible(l):
            if len1 % l or len2 % l:
                return False
            f1, f2 = len1//l, len2//l
            return str1 == str1[:l]*f1 and str2 == str1[:l]*f2

        for i in range(min(len(str1), len(str2)), 0, -1):
            if divisible(i):
                return str1[:i]
        return ""


        