class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        def backTrack(i, current):
            
            if current == n and len(path) == k:
                res.append(path[:])
                return

            if i >= 10 or current > n or len(path) > k:
                return

            backTrack(i+1, current)
            path.append(i)
            backTrack(i+1, current+i)
            path.pop()
        
        backTrack(1, 0)
        return res
        
