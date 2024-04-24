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
            k -= 1 - nums[r]
            if k < 0:
                k += 1 - nums[l]
                l += 1
            else:
                maxOnes = max(maxOnes, r - l + 1)
            r += 1
        return maxOnes

        