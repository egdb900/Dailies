class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        hashMap = {}
        for row in grid:
            key = ','.join(map(str, row))
            if key not in hashMap:
                hashMap[key] = 1
            else:
                hashMap[key] += 1
        
        for col in list(zip(*grid)):
            key = ','.join(map(str, col))
            if key in hashMap:
                result += hashMap[key]

                

        return result
        