class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        T = [0, 1, 1]
        for i in range(3, n+1):
            T.append(T[i-3] + T[i-2] + T[i-1])
        return T[n]


        