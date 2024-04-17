class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        diff1 = []
        for n in nums1:
            if n not in nums2:
                diff1.append(n)
        diff2 = []
        for n in nums2:
            if n not in nums1:
                diff2.append(n)
        return [set(diff1), set(diff2)]
        