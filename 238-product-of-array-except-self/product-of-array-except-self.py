class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1]
        right = [1]

        for i in range(0, len(nums)-1):
            left.append(left[i]*nums[i])

        for i in range(1, len(nums)):
            right.append(right[i-1]*nums[len(nums)-i])
        right = right[::-1]

        res = []
        for i in range(len(nums)):
            res.append(left[i]*right[i])

        return res

    
        

