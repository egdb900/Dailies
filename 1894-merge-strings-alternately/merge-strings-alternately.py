class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        s_len = min(len(word1), len(word2))

        for i in range(s_len):
            res += word1[i]
            res += word2[i]
        if len(word1) > s_len:
            res += word1[s_len:]
        if len(word2) > s_len:
            res += word2[s_len:]

        return res
