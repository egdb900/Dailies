class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr_sum = sum(nums[0:k])
        max_ave = float(curr_sum)/k
        for i in range(len(nums)-k):
            curr_sum -= nums[i]
            curr_sum += nums[i+k]
            if max_ave < float(curr_sum)/k:
                max_ave = float(curr_sum)/k
        return max_ave