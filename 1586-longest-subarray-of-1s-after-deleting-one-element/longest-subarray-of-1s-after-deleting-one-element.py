class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r, k = 0, 0, 1
        maxOnes = 0

        for num in nums:
            k -= 1 - nums[r]
            if k < 0:
                k += 1 - nums[l]
                l += 1
            else:
                maxOnes = max(maxOnes, r - l + 1)
            r += 1
        return maxOnes - 1
