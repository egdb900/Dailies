class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        T = [0, 1, 1]
        if n < 3:
            return T[n]

        for i in range(3, n+1):
            T.append(sum(T[i-3:i]))
        return T[-1]


        