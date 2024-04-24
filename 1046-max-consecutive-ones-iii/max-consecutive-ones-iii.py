class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l, r = 0, 0
        maxOnes = 0

        for num in nums:
            if nums[r] == 0:
                k -= 1
            if k < 0 and nums[l] == 0:
                k += 1
                l += 1
            elif k < 0 and nums[l] != 0:
                l += 1
            else:
                maxOnes = max(maxOnes, r - l + 1)
            r += 1
        return maxOnes

        