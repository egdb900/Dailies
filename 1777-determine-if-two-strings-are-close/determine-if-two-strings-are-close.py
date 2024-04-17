class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if set(word1) != set(word2) or len(word1) != len(word2):
            return False

        hashMap1 = {}
        for token in word1:
            if token not in hashMap1:
                hashMap1[token] = 1
            else:
                hashMap1[token] += 1

        hashMap2 = {}
        for token in word2:
            if token not in hashMap2:
                hashMap2[token] = 1
            else:
                hashMap2[token] += 1

        res1 = [hashMap1[x] for x in set(word1)]
        res2 = [hashMap2[x] for x in set(word2)]
        res1.sort()
        res2.sort()
        return res1 == res2