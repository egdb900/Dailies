class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = Counter(nums)
        nums.sort(key=lambda n: (count[n], -n))
        return nums

        