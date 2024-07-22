class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        lib = {}
        n = len(names)
        for i in range(n):
            lib[heights[i]] = names[i]

        keys = list(lib.keys())
        keys.sort(reverse=True)
        
        return [lib[i] for i in keys]