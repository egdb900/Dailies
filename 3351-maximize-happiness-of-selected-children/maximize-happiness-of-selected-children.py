class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort()
        max_happy = 0
        for i in range(k):
            max_happy += max(0, happiness.pop() - i)
        return max_happy


             