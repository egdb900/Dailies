class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        T = [0, 1, 1]
        if n < 3:
            return T[n]

        T_n = len(T)
        for i in range(n-T_n+1):
            T_i = sum(T[len(T)-T_n:len(T)])
            T.append(T_i)
        return T[-1]


        