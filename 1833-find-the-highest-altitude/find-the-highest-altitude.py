class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        max_alt = max(0, gain[0])
        for i in range(1, len(gain)):
            gain[i] = gain[i] + gain[i-1]
            max_alt = max(max_alt, gain[i])
        return max_alt