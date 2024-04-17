class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hashMap = {}
        for n in arr:
            if n not in hashMap:
                hashMap[n] = 1
            else:
                hashMap[n] += 1
        
        result = [hashMap[x] for x in set(arr)]
        return len(result) == len(set(result))
        